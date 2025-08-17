# Main Application Loop

**Issue Number**: #011  
**Status**: ✅ COMPLETED  
**Phase**: 3 - CLI Interface  
**Priority**: High  
**Estimated Effort**: Medium  

## Summary

Create the main application loop to process tasks in the CLI interface.

## Description

Implement the core application workflow that coordinates the Proposer, Governor, and Executor components to process user tasks. This is the heart of the agent's operation.

## Acceptance Criteria

- [x] Main application loop implemented in CLI entry point
- [x] Proper initialization of all agent components (Proposer, Governor, Executor)
- [x] Tool registry and integration
- [x] Task processing workflow implementation
- [x] Sequential action processing with approval checks
- [x] Error handling and graceful failure modes
- [x] Integration with logging system

## Implementation Notes

**Current Status**: ✅ COMPLETED
- `src/main.py` contains complete main application loop
- All agent components properly initialized and integrated
- Full tool registry with file system, web search, and system tools
- Comprehensive workflow from task input to execution
- Robust error handling throughout the process

## Application Workflow

```python
def main():
    # 1. Parse command-line arguments
    # 2. Initialize logging
    # 3. Create agent components
    # 4. Set up tool registry
    # 5. Process task through pipeline:
    #    - Propose actions
    #    - Governor approval
    #    - Execute approved actions
    # 6. Log all steps and results
```

## Component Integration

The main loop coordinates:
- **Proposer**: Analyzes tasks and suggests actions
- **Governor**: Reviews and approves/denies actions based on constitution
- **Executor**: Performs approved actions using registered tools
- **Logger**: Records all decisions and outcomes for audit

## Tool Registry

Currently integrated tools:
```python
tools = {
    "read_file": read_file,
    "write_file": write_file,
    "list_directory": list_directory,
    "search_web": search_web,
    "open_file": open_file,
    "remove_directory": remove_directory,
}
```

## Files Involved

- `src/main.py` - Main application loop and entry point
- All component modules (proposer.py, governor.py, executor.py)
- Tool modules in `src/tools/`
- Logging system integration

## Dependencies

- All agent components (Proposer, Governor, Executor)
- Tool implementations
- Configuration files (constitution.yaml)
- Logging system

## Related Issues

- [#002] Proposer Module - Generates actions for processing
- [#003] Governor Module - Approves actions in the loop
- [#004] Executor Module - Executes actions in the loop
- [#006] Logging System - Integrated throughout the loop
- [#009] Tool Integration - Tools are registered in main loop
- [#010] Argument Parsing - Provides input to the loop
- [#012] User Interaction - Provides output from the loop
- [#000] Master tracking issue

## Error Handling

The main loop includes comprehensive error handling:
- Component initialization failures
- Tool registration errors
- Task processing exceptions
- Constitution loading errors
- Graceful shutdown on errors

## Processing Flow

1. **Task Input**: Receive task from command-line arguments
2. **Proposal**: Proposer analyzes task and suggests actions
3. **Approval**: Governor reviews each action against constitution
4. **Execution**: Executor performs approved actions using tools
5. **Logging**: All steps logged for audit and debugging
6. **Output**: Results displayed to user

## Performance Considerations

- Sequential action processing ensures safety and audit trail
- Efficient tool lookup through dictionary registry
- Minimal overhead for component coordination
- Clean resource management and cleanup

---

**Original Task from DEV_PLAN.md**:  
"**Main Loop:** Create the main application loop to process tasks."

**Implementation Status**: Fully implemented with comprehensive component coordination. Provides the core processing engine that safely executes user tasks through the Proposer-Governor-Executor pipeline.