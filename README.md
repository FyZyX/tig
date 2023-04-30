# Tig

It's like Git, but in reverse: you make a commit, `tig` writes the code to make it happen!

## Background
We created `tig` as an attempt to help automate the software development process.
Inspired by the rise of Large Language Models (LLMs) and code generation capabilities,
`tig` reverses the traditional developer workflow by allowing developers to focus on
the intent of the changes rather than manually implementing them. We realized that
version control systems (VCS) like `git` inherently connect software changes to natural
language commit messages, so it seemed only natural to turn that on its head.

Additionally, we want to introduce automated tooling to the software development community
in a way that aligns with the tools and workflows they've become accustomed to. Rather than
think of advancements in AI as stealing developers jobs, we want to build tools that evolve
the discipline of software engineering gradually. Hopefully, these tools will allow developers
to shift their workloads away from monotonous or repetitive tasks and allow them to focus on
shaping the development process to meet the needs of their users.

## Current Implementation
This version of `tig` is intentionally simplistic, and in this current stage, it should be
understood as nothing more than proof of concept.

Right now, you can point `tig` at a specific file and submit a commit message.
We then submit that entire file plus the commit message to OpenAI's completion endpoint and prompt it to return a revised version of the code.
Finally, we overwrite the original file with the output from that response.

## Usage

To try the tool out
- clone this repository
- make sure you expose your OpenAI API key as the environment variable `OPENAI_API_KEY`
- create a simple example file (here I'll use some Python boilerplate)
```python
def main():
    pass


if __name__ == '__main__':
    main()
```
- Open a command prompt and run the app like so:
```shell
$ python app.py commit -m "add a function that generates random numbers" -t example.py
```

Here `app.py` acts as a command line tool similar to `git`.
However, in this simple model, you must specify the target file you want to affect, in this case `example.py`,
as well as the commit message you want to apply.

> **NOTE:** This tool is eventually meant to be installed on the client system and run within a project directory,
> but at this stage we're simply running it as if `tig` itself is the project directory. 

## Next Steps
1. Replacing the entire file is extremely wasteful. Imagine you have a file that contains 2,000 tokens, and the change you need to make only alters 20 of those tokens. You now have to pay for an API request with 4k tokens for one tiny change.
2. Obviously commits on larger codebases generally touch multiple files. Therefore, we need a mechanism to determine which parts of the code need to be altered.
3. We should probably have a way to validate that the updated code actually does what the commit intended. The most obvious solution in my mind is to have the agent produce test cases first, then write code to satisfy those test cases, then run the tests and recursively attempt to debug any errors.
4. Integration with VCS. It would be nice to have the resulting changes actually committed to version control with the original commit message as a final step.
