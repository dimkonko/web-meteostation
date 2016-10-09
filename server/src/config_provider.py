import os


def init_config(app):
    CFG_TYPE = os.environ.get('CFG_TYPE')
    if not CFG_TYPE:
        CFG_TYPE = 'dev'

    app.config.from_json('../conf/%s.json' % CFG_TYPE)
