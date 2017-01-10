Slack Handler
=============

This module provides a logging handler that takes a slack hook url as its only
argument. Logs sent to that handler are then buffered and passed to the slack
channel attached to that hook.


## Usage

    import logging

    from slack_logging_handler import SlackHandler

    logger = logging.getLogger(__name__)
    handler = SlackHandler('https://hooks.slack.com/services/qwerty/qwertyqwerty')

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


## Or with yamlized config


    # logging.yml
    ---
    version: 1
    disable_existing_loggers: False
    formatters:
        simple:
            format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
        slack_channel_handler:
            class: slack_logging_handler.SlackHandler
            level: INFO
            formatter: simple
            hook_url: 'https://hooks.slack.com/services/qwerty/qwertyqwerty'
            capacity: 10
    root:
        level: DEBUG
        handlers: [slack_channel_handler]


    # somepythonfile.py

    import logging
    import logging.config
    import yaml

    with open('logging.yml') as f:
        logging.config.dictConfig(yaml.load(f))
    logger = logging.getLogger(__name__)

Tests
-----
To run the tests, define an environment variable with the token for your slack
hook as SLACK_HOOK_TOKEN. Test message will be sent to that channel during
testing.
