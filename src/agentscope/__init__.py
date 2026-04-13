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


def init(
    model_configs: Optional[list] = None,
    project: Optional[str] = None,
    run_id: Optional[str] = None,
    save_dir: str = "./runs",
    save_log: bool = True,
    save_code: bool = True,
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
            Defaults to ``"./runs"``.
        save_log (bool): Whether to persist log output to disk.
            Defaults to ``True``.
        save_code (bool): Whether to save a snapshot of the calling
            script alongside run artifacts. Defaults to ``True``.
        save_api_invoke (bool): Whether to record all API invocation
            details for debugging. Defaults to ``False``.
        use_monitor (bool): Whether to enable the token/cost monitor.
            Defaults to ``True``.
        logger_level (str): Logging verbosity level. One of
            ``"DEBUG"``, ``"INFO"``, ``"WARNING"``, ``"ERROR"``.
            Defaults to ``"INFO"``.
        runtime_param (dict, optional): Additional runtime parameters
            passed through to the underlying runtime manager.

    Raises:
        ValueError: If an unrecognized ``logger_level`` is supplied.
        FileNotFoundError: If ``save_dir`` cannot be created.

    Example:
        .. code-block:: python

            import agentscope

            agentscope.init(
                model_configs=[
                    {
                        "model_type": "openai_chat",
                        "config_name": "gpt-4o",
                        "model_name": "gpt-4o",
                        "api_key": "YOUR_API_KEY",
                    }
                ],
                project="my_experiment",
                save_dir="./output",
            )
    """
    # Import here to avoid circular imports at module load time
    from agentscope.manager import ASManager  # noqa: PLC0415

    ASManager.get_instance().initialize(
        model_configs=model_configs or [],
        project=project,
        run_id=run_id,
        save_dir=save_dir,
        save_log=save_log,
        save_code=save_code,
        save_api_invoke=save_api_invoke,
        use_monitor=use_monitor,
        logger_level=logger_level,
        runtime_param=runtime_param or {},
    )


__all__ = [
    "__version__",
    "init",
]
