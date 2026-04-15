# -*- coding: utf-8 -*-
"""AgentScope - A flexible and powerful agent framework.

This package provides the core functionality for building and managing
AI agents with support for multiple LLM backends, memory management,
and multi-agent orchestration.
"""

__version__ = "0.1.0"
__author__ = "AgentScope Contributors"
__license__ = "Apache 2.0"

from typing import Optional

# Personal preference: default save_dir to a hidden dot-folder so run
# artifacts don't clutter the project root during local experimentation.
_DEFAULT_SAVE_DIR = "./.agentscope_runs"

# Valid logger levels for input validation
_VALID_LOGGER_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def init(
    model_configs: Optional[list] = None,
    project: Optional[str] = None,
    run_id: Optional[str] = None,
    save_dir: str = _DEFAULT_SAVE_DIR,
    save_log: bool = True,
    save_code: bool = False,
    save_api_invoke: bool = False,
    use_monitor: bool = True,
    logger_level: str = "INFO",
    runtime_param: Optional[dict] = None,
) -> None:
    """Initialize the AgentScope framework.

    This function sets up the runtime environment, configures logging,
    registers model configurations, and prepares the monitoring system.

    Args:
        model_configs (list, optional): A list of model configuration
            dictionaries. Each dict should contain at minimum a
            ``model_type`` and ``config_name`` field.
        project (str, optional): The name of the current project or
            experiment. Used for organizational purposes.
        run_id (str, optional): A unique identifier for this run.
            Auto-generated if not provided.
        save_dir (str): Directory path where run artifacts are saved.
            Defaults to ``"./.agentscope_runs"`` (a hidden folder so
            run artifacts don't clutter the project root).
        save_log (bool): Whether to persist log output to disk.
            Defaults to ``True``.
        save_code (bool): Whether to save a snapshot of the calling
            script alongside run artifacts. Defaults to ``False``.
            (Personal note: changed default to False since I rarely
            need code snapshots during local experimentation.)
        save_api_invoke (bool): Whether to record all API invocation
            details for debugging. Defaults to ``False``.
        use_monitor (bool): Whether to enable the token/cost monitor.
            Defaults to ``True``.
        logger_level (str): Logging verbosity level. One of
            ``"DEBUG"``, ``"INFO"``, ``"WARNING"``, ``"ERROR"``,
            ``"CRITICAL"``.
            Defaults to ``"INFO"`` for cleaner output. Switch to
            ``"DEBUG"`` when actively troubleshooting issues.
            (Personal note: changed default from DEBUG to INFO since
            DEBUG output is too noisy for day-to-day use.)
        runtime_param (dict, optional): Additional runtime parameters
            passed through to the underlying runtime manager.

    Raises:
        ValueError: If ``logger_level`` is not one of the accepted
            values in ``_VALID_LOGGER_LEVELS``.
    """
    # Validate logger_level early so the error message is clear rather
    # than surfacing as a cryptic failure deep in the logging setup.
    if logger_level not in _VALID_LOGGER_LEVELS:
        raise ValueError(
            f"Invalid logger_level '{logger_level}'. "
            f"Must be one of: {', '.join(_VALID_LOGGER_LEVELS)}"
        )
