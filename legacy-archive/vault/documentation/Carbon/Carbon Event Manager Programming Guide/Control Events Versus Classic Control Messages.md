---
title: Carbon Event Manager Programming Guide
apple_id: TP30000989
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon_Event_Manager/ApdxCmessages/CarbonEventsApdxmessages.html
archived_at: '2026-07-15T05:22:31.523457Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Event Manager Programming Guide](Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md)


[Next](Glossary.md)[Previous](Document%20Revision%20History.md)

# Control Events Versus Classic Control Messages

The control event constants defined by the Carbon Event Manager generally map to control messages sent to control defprocs (CDEFs) as shown in [Table A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqhewvgvzr).

__Table A-1__  Control Events versus Control defproc messages

| Control event constant | Control defproc message(s) |
| `kEventControlInitialize` | `initCntl``kControlMsgTestNewMsgSupport``kControlMsgGetFeatures` (in that order) |
| `kEventControlDispose` | `dispCntl` |
| `kEventControlGetOptimalBounds` | `kControlMsgCalcBestRect` |
| `kEventControlDefInitialize` | Same as for `kEventControlInitialize`. |
| `kEventControlDefDispose` | Same as for `kEventControlDispose` |
| `kEventControlHit` | No equivalent message |
| `kEventControlSimulateHit` | No equivalent message |
| `kEventControlHitTest` | `testCntl` |
| `kEventControlDraw` | `drawCntl` |
| `kEventControlApplyBackground` | `kControlMsgSetUpBackground` |
| `kEventControlApplyTextColor` | `kControlMsgApplyTextColor` |
| `kEventControlSetFocusPart` | `kControlMsgFocus` |
| `kEventControlGetFocusPart` | No equivalent message. |
| `kEventControlActivate` | `kControlMsgActivate` (with param = 1) |
| `kEventControlDeactivate` | `kControlMsgActivate` (with param = 0) |
| `kEventControlSetCursor` | `kControlMsgSetCursor` |
| `kEventControlContextualMenuClick` | `kControlMsgContextualMenuClick` |
| `kEventControlTrack` | `kControlMsgHandleTracking` |
| `kEventControlGetScrollToHereStartPoint` | No equivalent message. |
| `kEventControlGetIndicatorDragConstraint` | `thumbCntl` |
| `kEventControlIndicatorMoved` | `kControlMsgDrawGhost` (for nonlive tracking) or `kControlMsgCalcValueFromPos` (for live tracking). |
| `kEventControlGhostingFinished` | `posCntl` |
| `kEventControlGetActionProcPart` | No equivalent message. |
| `kEventControlGetPartRegion` | `kControlMsgGetRegion` for controls that support `GetRegion`, `calcCntlRgn` or `calcThumbRgn` otherwise. |
| `kEventControlGetPartBounds` | No equivalent message. |
| `kEventControlSetData` | `kControlMsgSetData` |
| `kEventControlGetData` | `kControlMsgGetData` |
| `kEventControlValueFieldChanged` | `drawCntl` with param = `kControlIndicatorPart` |
| `kEventControlAddedSubControl` | `kControlMsgSubControlAdded` |
| `kEventControlRemovingSubControl` | `kControlMsgSubControlRemoved` |
| `kEventControlArbitraryMessage` | Anything sent using `SendControlMessage` |
| `kEventWindowGetClickActivation` (of event class `kEventClassWindow`) | `kControlMsgGetClickActivation` |

Some messages are no longer supported, as shown in Table A-2

__Table A-2__  Unsupported CDEF messages

| Message | Why No Carbon Event Equivalent |
| `calcCRgns` | Obsolete. Use `kControlMsgGetRegion` instead. |
| `autoTrack` | Use `kControlMsgHandleTracking` instead. |
| `dragCntl` | Obsolete. No one needs to use this anymore. |
| `drawThumbOutline` | Obsolete. Use `kControlDrawMsgGhost`, `kControlMsgCalcValueFromPos`, and `posCntl` instead. |
| `kControlMsgKeyDown` | Only marginal support available on Mac OS X using `kEventControlArbitraryMessage`. Use `kEventTextInput` class of Carbon events instead. |
| `kControlMsgIdle` | Only marginal support available on Mac OS X using `kEventControlArbitraryMessage`. The CDEF should install a timer instead. |
| `kControlMsgSubValueChanged` | Only marginal support available on Mac OS X using `kEventControlArbitraryMessage`. CDEF should install `kEventControlValueFieldChanged` on its children instead. |
| `kControlMsgFlatten` | Obsolete. Never implemented. |

[Next](Glossary.md)[Previous](Document%20Revision%20History.md)

