# PyHowDoI

A utility for quick command-line guidance from ChatGPT.

**⚠️ Use at your own risk. Carefully inspect all commands before running them. ⚠️**

For example:

```
howdoi get a list of all files modified in the last five minute
```

Response:

```
find . -type f -mmin -5
```

No more trips to StackOverflow or man pages for simple things!

## Installation

```
pip install pyhowdoi
```

## Usage

You must set the environment variable `OPENAPI_API_KEY` in order for this utility
to function. You will be charged for any usage of the API.

```
howdoi <any question here>
howdoi spin up a simple HTTP server
howdoi check how much disk space is currently being used
howdoi make a cron string that runs every wednesday at 5 am
howdoi find all lines that have TODO in them
```

If you wish to use special characters that might normally be interpreted by the
shell, you can wrap your question in quotes:

```
howdoi 'replace all instance of $ with € in a file'
```

By default, the model `gpt-3.5-turbo` is used, but you can override this by
setting the `OPENAI_CHAT_MODEL` environment variable:

```
export OPENAI_CHAT_MODEL=gpt-4
howdoi check that the hash of a file is correct
```

See https://platform.openai.com/docs/models/overview for a full list of available models.

You can also pipe in standard input to provide additional context for the utility.
For instance, you could pass in the help message or man page for a command:

```
curl -h 2>&1 | howdoi use curl to upload a file
```
