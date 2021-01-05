#!/usr/bin/env python3
from acru_l.apps.base import setup_app


# For local testing of the aws configuration
app = setup_app()
app.synth()
