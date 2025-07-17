See https://docs.openwebui.com/pipelines/

Please note that Pipelines and [Open WebUI functions](https://docs.openwebui.com/features/plugin/functions/) (Pipe Function, Filter Function and Action function) are different features.

See Open WebUI fonction example in [`../functions`](../functions/).

Use this script to import a function of type [Pipelines](https://docs.openwebui.com/pipelines/):

```sh
$ ../scripts/upload-pipelines-function.py ../pipelines/hello_world.py
{"status":true,"detail":"Pipeline uploaded successfully to ./pipelines/hello_world.py"}
```

The `*.json` files contain the Valves parameters for the Pipelines function, which can be uploaded with:

```sh
$ ./scripts/upload-pipelines-function-valves.py pipelines/hello_world_valves.json
{"FOO":"secret"}
```

Example content of a `...valves.json` file:

```
{
    "function_filename": "hello_world.py",
    "valves": {
        "FOO": "secret"
    }
}
```

Be sure to fill in the `function_filename` field with the complete name of the Pipelines function file for the Valves.
