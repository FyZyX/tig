# `tig`

## Overview

`tig` is like `git` in reverse! It is a software development tool that allows users to commit code changes using natural language.
The key innovation is `tig`'s ability to interpret these descriptive commits, plan the required code modifications, and automatically implement the changes in the codebase.

`tig` aims to significantly reduce the burden of manual coding by translating a user's high-level feature requests and bug fixes into working software implementations.

## How it Works

1. The user initiates the process by providing a natural language commit message describing the desired change, similar to how one would write a git commit.
2. `tig` parses this message to identify the required changes
3. Leveraging its repository of code snippets and its understanding of the app architecture, Tig formulates a plan to implement the change.
4. `tig` then executes the plan, automatically modifying files across the codebase - adding new files, editing existing ones, importing dependencies etc.
5. Once complete, `tig` displays a diff of all changes for the user to review. After approving, `tig` commits the changes to the repository.

## Capabilities

- Natural language parsing: Understand descriptive commit messages
- Change planning: Formulate a plan to implement the desired modification
- Automated coding: Programmatically modify codebase to execute the plan
- Project management: Maintain backlog of commits, prioritize based on effort/impact

## Benefits

- 10X faster development: Eliminates time-consuming manual coding
- Focus on design: Users spend time on high-level design rather than implementation
- Accelerated learning: System continuously expands its repertoire of code snippets and planning abilities
- Better documentation: Descriptive commit messages serve as documentation
- Consistent style: Changes adhere to preset project conventions and patterns
