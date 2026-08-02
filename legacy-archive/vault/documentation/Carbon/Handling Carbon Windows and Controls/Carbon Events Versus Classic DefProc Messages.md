---
title: Handling Carbon Windows and Controls
apple_id: TP30001004
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HandlingWindowsControls/hitb-apdx_a_msgs/hitb-apdx_a_msgs.html
archived_at: '2026-07-15T05:22:46.946869Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Handling Carbon Windows and Controls](Introduction%20to%20Handling%20Carbon%20Windows%20and%20Controls.md)


[Next](Document%20Revision%20History.md)[Previous](Window%20and%20Control%20Tasks.md)

# Carbon Events Versus Classic DefProc Messages

The window event constants defined by the Carbon Event Manager map to the window messages sent to window defprocs (WDEFs) as shown in [Table A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqg4wueq2ji5feoqke).

__Table A-1__  Window events versus window defproc messages

| Window event constant | Window defproc message |
| `kEventWindowDrawFrame` | `kWindowMsgDraw` |
| `kEventWindowDrawPart` | `kWindowMsgDraw` |
| `kEventWindowHitTest` | `kWindowMsgTestHit` |
| `kEventWindowInit` | `kWindowMsgInitialize` |
| `kEventWindowDispose` | `kWindowMsgCleanUp` |
| `kEventWindowGrowBox` | `kWindowMsgDrawGrowBox` |
| `kEventWindowGetRegion` | `kWindowMsgGetRegion` |
| `kEventWindowDragHilite` | `kWindowMsgDragHilite` |
| `kEventWindowModified` | `kWindowMsgModified` |
| `kEventWindowSetUpProxyDragImage` | `kWindowMsgSetUpProxyDragImage` |
| `kEventWindowStateChanged` | `kWindowMsgStateChanged` |
| `kEventWindowMeasureTitle` | `kWindowMsgMeasureTitle` |
| `kEventWindowGetGrowImageRegion` | `kWindowMsgGetGrowImageRegion` |
| `kEventWindowPaint` | No equivalent message |

[Table A-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqg4wueq2ji5euiqsi) shows window defproc messages that have no direct Carbon Event equivalent.

__Table A-2__  Deprecated or unsupported WDEF messages

| Message | Why no Carbon event equivalent |
| `kWindowMsgCalculateShape` | Obsolete in Carbon. The Window Manager sends two `kEventWindowGetRegion` events (or two `kWindowMsgGetRegion` messages): one for the structure region, another for the content region. |
| `kWindowMsgDrawGrowOutLine` | Functionality replaced by `kEventWindowGetGrowImageRegion`. Instead of asking the custom window to draw the grow outline, the Window Manager asks for the grow image outline and draws it itself. |
| `kWindowMsgGetFeatures` | Functionality is now included in the `kEventWindowInit` event. When called, the initialization handler should place the window features into the `kEventParamWindowFeatures` parameter before returning. |
| `kWindowMsgDrawInCurrentPort` | Essentially replaced by `kEventWindowDrawFrame`, which implies drawing into the current port. |

The control event constants defined by the Carbon Event Manager generally map to control messages sent to control defprocs (CDEFs) as shown in [Table A-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqg4wuescgineeurcf).

__Table A-3__  Control events versus Control defproc messages

| Control event constant | Control defproc messages |
| `kEventControlInitialize` | `initCntl``kControlMsgTestNewMsgSupport``kControlMsgGetFeatures` (in that order) |
| `kEventControlDispose` | `dispCntl` |
| `kEventControlGetOptimalBounds` | `kControlMsgCalcBestRect` |
| `kEventControlDefInitialize` | Same as for `kEventControlInitialize`s |
| `kEventControlDefDispose` | Same as for `kEventControlDispose` |
| `kEventControlHit` | No equivalent message |
| `kEventControlSimulateHit` | No equivalent message |
| `kEventControlHitTest` | `testCntl` |
| `kEventControlDraw` | `drawCntl` |
| `kEventControlApplyBackground` | `kControlMsgSetUpBackground` |
| `kEventControlApplyTextColor` | `kControlMsgApplyTextColor` |
| `kEventControlSetFocusPart` | `kControlMsgFocus` |
| `kEventControlGetFocusPart` | No equivalent message |
| `kEventControlActivate` | `kControlMsgActivate` (with param = 1) |
| `kEventControlDeactivate` | `kControlMsgActivate` (with param = 0) |
| `kEventControlSetCursor` | `kControlMsgSetCursor` |
| `kEventControlContextualMenuClick` | `kControlMsgContextualMenuClick` |
| `kEventControlTrack` | `kControlMsgHandleTracking` |
| `kEventControlGetScrollToHereStartPoint` | No equivalent message |
| `kEventControlGetIndicatorDragConstraint` | `thumbCntl` |
| `kEventControlIndicatorMoved` | `kControlMsgDrawGhost` (for non-live tracking) or `kControlMsgCalcValueFromPos` (for live tracking) |
| `kEventControlGhostingFinished` | `posCntl` |
| `kEventControlGetActionProcPart` | No equivalent message |
| `kEventControlGetPartRegion` | `kControlMsgGetRegion` for controls that support `GetRegion`, `calcCntlRgn` or `calcThumbRgn` otherwise |
| `kEventControlGetPartBounds` | No equivalent message |
| `kEventControlSetData` | `kControlMsgSetData` |
| `kEventControlGetData` | `kControlMsgGetData` |
| `kEventControlValueFieldChanged` | `drawCntl` with param = `kControlIndicatorPart` |
| `kEventControlAddedSubControl` | `kControlMsgSubControlAdded` |
| `kEventControlRemovingSubControl` | `kControlMsgSubControlRemoved` |
| `kEventControlArbitraryMessage` | Anything sent using `SendControlMessage` |
| `kEventWindowGetClickActivation` (of event class `kEventClassWindow`) | `kControlMsgGetClickActivation` |

Some control messages are no longer supported, as shown in [Table A-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqg4wuescgizbuor2f)

__Table A-4__  Unsupported CDEF messages

| Message | Why no Carbon event equivalent |
| `calcCRgns` | Obsolete. Use `kControlMsgGetRegion` instead. |
| `autoTrack` | Use `kControlMsgHandleTracking` instead. |
| `dragCntl` | Obsolete. No one needs to use this anymore. |
| `drawThumbOutline` | Obsolete. Use `kControlDrawMsgGhost`, `kControlMsgCalcValueFromPos`, and `posCntl` instead. |
| `kControlMsgKeyDown` | Only marginal support available in Mac OS X using `kEventControlArbitraryMessage`. Use `kEventTextInput` class of Carbon events instead. |
| `kControlMsgIdle` | Only marginal support available in Mac OS X using `kEventControlArbitraryMessage`. The CDEF should install a timer instead. |
| `kControlMsgSubValueChanged` | Only marginal support available in Mac OS X using `kEventControlArbitraryMessage`. CDEF should install `kEventControlValueFieldChanged` on its children instead. |
| `kControlMsgFlatten` | Obsolete. Never implementted. |

[Next](Document%20Revision%20History.md)[Previous](Window%20and%20Control%20Tasks.md)

