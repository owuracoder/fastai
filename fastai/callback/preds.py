# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/18b_callback.preds.ipynb.

# %% ../nbs/18b_callback.preds.ipynb 2
from __future__ import annotations
from ..basics import *

# %% auto 0
__all__ = ['MCDropoutCallback']

# %% ../nbs/18b_callback.preds.ipynb 7
class MCDropoutCallback(Callback):
    def before_validate(self):
        for m in [m for m in flatten_model(self.model) if 'dropout' in m.__class__.__name__.lower()]:
            m.train()
    
    def after_validate(self):
        for m in [m for m in flatten_model(self.model) if 'dropout' in m.__class__.__name__.lower()]:
            m.eval()
