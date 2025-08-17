# Governor Module

**Issue Number**: #003  
**Status**: ✅ COMPLETED  
**Phase**: 1 - Core Framework  
**Priority**: High  
**Estimated Effort**: Medium  

## Summary

Implement the `Governor` class to approve or deny actions based on the `constitution.yaml` file.

## Description

The Governor serves as the ethical and safety control layer of the agent. It reviews each proposed action against the constitution rules and either approves or denies the action, ensuring the agent operates within defined boundaries.

## Acceptance Criteria

- [x] Governor class created in `src/governor.py`
- [x] `approve_action(action)` method implemented
- [x] Integration with `constitution.yaml` file
- [x] YAML configuration parsing with PyYAML
- [x] Boolean approval/denial system
- [x] Unit tests for the Governor class

## Implementation Notes

**Current Status**: ✅ COMPLETED
- `src/governor.py` exists with Governor class
- Loads constitution from YAML file during initialization
- `approve_action()` method checks action against `allowed_actions` list
- Uses PyYAML for configuration parsing
- Robust error handling for missing/invalid constitution files
- Comprehensive test coverage in `tests/test_governor.py`

## Technical Details

```python
class Governor:
    def __init__(self, constitution_path):
        with open(constitution_path, 'r') as f:
            self.constitution = yaml.safe_load(f)

    def approve_action(self, action):
        if action["action"] in self.constitution["allowed_actions"]:
            return True
        return False
```

## Configuration

The `constitution.yaml` file currently allows:
- search_web
- read_file
- write_file
- list_directory
- open_file
- remove_directory

## Files Involved

- `src/governor.py` - Main implementation
- `constitution.yaml` - Configuration file
- `tests/test_governor.py` - Unit tests
- `tests/test_constitution.yaml` - Test configuration

## Dependencies

- PyYAML==6.0.1 for YAML parsing
- constitution.yaml configuration file

## Related Issues

- [#002] Proposer Module - Generates actions for review
- [#004] Executor Module - Executes approved actions
- [#005] Constitution System - Defines the rules
- [#029] Constitution Evolution - Future self-modification capabilities
- [#000] Master tracking issue

## Security Notes

The Governor is a critical security component. All actions must pass through this approval system, making it a key control point for agent behavior.

---

**Original Task from DEV_PLAN.md**:  
"**Governor Module:** Implement the `Governor` class to approve or deny actions based on the `constitution.yaml` file."

**Implementation Status**: Fully implemented with robust YAML-based configuration system. Provides essential safety controls for all agent actions.