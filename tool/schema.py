add_module = {
    "name": "add_module",
    "description": "Create a new module in this project.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Name of the module to be created"
            }
        },
        "required": [
            "name"
        ]
    }
}
