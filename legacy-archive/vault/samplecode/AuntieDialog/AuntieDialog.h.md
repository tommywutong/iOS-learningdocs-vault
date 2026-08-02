---
title: AuntieDialog
apple_id: DTS10000556
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/AuntieDialog/Listings/AuntieDialog_h.html
archived_at: '2026-07-18T03:01:34.535626Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AuntieDialog](AuntieDialog.md)


[Next](AuntieDialog.html.md)[Previous](AuntieDialog.cp.md)

# AuntieDialog.h

```c
#ifdef __MWERKS__

// includes for MetroWerks CodeWarrior

#include <Controls.h>
#include <Windows.h>

#else

#ifdef __APPLE_CC__

// includes for ProjectBuilder

#include <Carbon/Carbon.h>

#else

// includes for MPW

#include <Carbon.h>

#endif
#endif

#ifdef __cplusplus
extern "C" {
#endif

enum
{
    kAuntieDialogSignature                          = 'aunt',
    kAuntieDialogControlPropertyTagTriedFocus       = 'trfo',
    kAuntieDialogControlPropertyTagProcID           = 'proc',
    kAuntieDialogControlPropertyTagTicksAtLastIdle  = 'tali',
    kAuntieDialogWindowPropertyTagIsAuntieDialog    = 'iadw'
};

typedef pascal OSStatus (*ControlHierarchySearchProcPtr)    (   ControlRef,
                                                                Boolean         *stop,
                                                                void            *userData       );

typedef pascal OSStatus (*ControlCreationProcPtr)           (   ControlRef,
                                                                void            *ccppUserData   );

typedef pascal OSStatus (*FocusChangeValidationProcPtr)     (   ControlRef,
                                                                Boolean         *allow          );

typedef pascal OSStatus (*AuntieModalFilterProcPtr)         (   WindowRef,
                                                                EventRecord     *,
                                                                ControlRef      *itemHit        );


pascal UInt32
AuntieDialogGetIdleInterval         (           WindowRef                       window          );

pascal OSStatus
SetDefaultControl                   (           ControlRef,
                                                Boolean                         willBeDefault   );
pascal OSStatus
InvalControl                        (           ControlRef,
                                                Boolean                         includeChildren );
pascal OSStatus
CountControlsInWindow               (           WindowRef,
                                                UInt16                          *               );

pascal OSStatus
DisposeChildControls                (           ControlRef                                      );

pascal OSStatus
IsAuntieDialogEvent                 (   const   EventRecord                     *event,
                                                WindowRef                       *window         );
pascal OSStatus
AuntieDialogSelect                  (   const   EventRecord                     *event,
                                                RgnHandle                       mouseRgn,
                                                ControlRef                      *itemHit,
                                                FocusChangeValidationProcPtr                    );
pascal OSStatus
AuntieModalDialog                   (           WindowRef                       window,
                                                ControlRef                      *itemHit,
                                                AuntieModalFilterProcPtr,
                                                FocusChangeValidationProcPtr                    );
pascal OSStatus
StandardAuntieModalEventFilter      (           WindowRef,
                                                EventRecord                     *,
                                                ControlRef                      *itemHit        );
pascal OSStatus
AppendDialogItemsAsControls         (           short                           resID,
                                                WindowRef,
                                                ControlCreationProcPtr,
                                                void                            *ccppUserData   );
pascal OSStatus
NewAuntieDialog                     (           short                           resID,
                                                WindowRef,
                                                ControlCreationProcPtr,
                                                void                            *ccppUserData   );
pascal OSStatus
GetAuntieDialog                     (           short                           resID,
                                                WindowRef                       behind,
                                                ControlCreationProcPtr,
                                                void                            *ccppUserData,
                                                WindowRef                       *result         );
pascal OSStatus
SearchControlHierarchy              (           WindowRef,
                                                ControlHierarchySearchProcPtr,
                                                ControlRef                      *found,
                                                void                            *userData       );

pascal OSStatus
ReestablishFocusOnNextNullEvent     (           WindowRef                       window          );

pascal OSStatus
AuntieDialogDisableControl          (           ControlRef                      control         );

pascal OSStatus
AuntieDialogEnableControl           (           ControlRef                      control         );

pascal OSStatus
AuntieDialogEnableDisableControl    (           ControlRef                      control,
                                                Boolean                         enableDisable   );

#ifdef __cplusplus
}
#endif
```

[Next](AuntieDialog.html.md)[Previous](AuntieDialog.cp.md)

