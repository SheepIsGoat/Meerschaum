#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Register a Pipe object
"""

def register(
        self,
        debug : bool = False
    ):
    """
    Send a POST to the Meerschaum API to register a new Pipe.
    """
    if self.connector.type == 'plugin' and self.connector.register is not None:
        params = self.connector.register(self)
        params = {} if params is None else params
        if not isinstance(params, dict):
            from meerschaum.utils.warnings import warn
            warn(
                f"Invalid parameters returned from `register()` in plugin {self.connector}:\n"
                + f"{params}"
            )
        else:
            self.parameters = params

    if not self.parameters:
        self.parameters = {
            'columns' : self.columns,
        }

    return self.instance_connector.register_pipe(self, debug=debug)

