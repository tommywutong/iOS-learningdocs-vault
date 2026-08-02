---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEMenuUtils_h.html
archived_at: '2026-07-18T03:14:37.924878Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEMove.c.md)[Previous](Sources-MSAEMenuUtils.c.md)

# Sources/MSAEMenuUtils.h

```c
#pragma once

#include "MSToken.h"


OSErr   MenuNameToMenuToken( StringPtr theName, MenuToken *theToken );
OSErr   GetDescOfNamedMenu( StringPtr theName, AEDesc* result );
OSErr   GetDescOfNthMenu( short theIndex, AEDesc* result );
short   CountMenus( void );
void    GetMenuName( MenuToken* theToken, StringPtr theResult );
void    SetMenuItemName( MenuItemToken* theToken, StringPtr theResult );

OSErr   MenuItemNameToMenuItemToken( MenuToken* containerToken,
                                    StringPtr theName, MenuItemToken *theToken );
OSErr   GetDescOfNamedMenuItem( MenuToken* containerToken, StringPtr theName, AEDesc* result );
OSErr   GetDescOfNthMenuItem( MenuToken* containerToken, short theIndex, AEDesc* result );
short   CountMenuTokenItems( MenuToken* containerToken );
void    GetMenuItemName( MenuItemToken* theToken, StringPtr theResult );

OSErr   MakeMenuSpecifier( MenuToken* theToken, AEDesc* theResult );
OSErr   MakeMenuItemSpecifier( MenuItemToken* theToken, AEDesc* theResult );

void    MenuTokenFromResID( short theResID, MenuToken* theToken );
void    MenuItemTokenFromResID( short theResID, MenuItemToken* theToken );

MenuHandle  MenuHandleFromMenuID( short theMenuID );
```

[Next](Sources-MSAEMove.c.md)[Previous](Sources-MSAEMenuUtils.c.md)

