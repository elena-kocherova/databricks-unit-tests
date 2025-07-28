# Databricks notebook source
# MAGIC %pip install pytest

# COMMAND ----------

import pytest
# import os
import sys

# Run all tests in the repository root.
# notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
# repo_root = "/Workspace/Users/elena.kocherova@nationalhighways.co.uk/unit_tests/" #os.path.dirname(os.path.dirname(notebook_path))
# os.chdir(f'{repo_root}')
# %pwd

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."
