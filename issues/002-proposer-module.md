# Proposer Module

**Issue Number**: #002  
**Status**: ✅ COMPLETED  
**Phase**: 1 - Core Framework  
**Priority**: High  
**Estimated Effort**: Medium  

## Summary

Create the `Proposer` class that suggests actions based on a given task.

## Description

The Proposer is responsible for analyzing user tasks and generating a sequence of actions that the agent should perform. It serves as the "thinking" component of the agent.

## Acceptance Criteria

- [x] Proposer class created in `src/proposer.py`
- [x] `propose_action(task)` method implemented
- [x] Basic keyword-based action mapping
- [x] Returns structured action objects with action type and arguments
- [x] Unit tests for the Proposer class

## Implementation Notes

**Current Status**: ✅ COMPLETED
- `src/proposer.py` exists with Proposer class
- Basic keyword matching implemented for common tasks:
  - "list files" → list_directory action
  - "doc" → open_file for USER_GUIDE.md
  - "clean" → remove build/dist directories
  - "history of artificial intelligence" → web search
- Returns properly structured action dictionaries
- Comprehensive test coverage in `tests/test_proposer.py`

## Technical Details

```python
class Proposer:
    def propose_action(self, task):
        actions = []
        if "list files" in task:
            actions.append({"action": "list_directory", "args": ["."]})
        # ... additional keyword matching
        return actions
```

## Files Involved

- `src/proposer.py` - Main implementation
- `tests/test_proposer.py` - Unit tests

## Dependencies

- None (standalone module)

## Related Issues

- [#003] Governor Module - Approves/denies proposed actions
- [#004] Executor Module - Executes approved actions
- [#000] Master tracking issue

## Future Enhancements

See [#022] Natural Language Understanding for advanced NLP-based proposal generation.

---

**Original Task from DEV_PLAN.md**:  
"**Proposer Module:** Create the `Proposer` class that suggests actions based on a given task."

**Implementation Status**: Fully implemented with basic keyword matching. Works effectively for common tasks and integrates well with the Governor-Executor workflow.