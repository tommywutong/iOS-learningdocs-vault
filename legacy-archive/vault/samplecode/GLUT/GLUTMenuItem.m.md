---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/GLUTMenuItem_m.html
archived_at: '2026-07-18T03:29:12.422665Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](GLUTPreferencesController.h.md)[Previous](GLUTMenuItem.h.md)

# GLUTMenuItem.m

```objc

/* Copyright (c) Dietmar Planitzer, 2002 */

/* This program is freely distributable without licensing fees 
   and is provided without guarantee or warrantee expressed or 
   implied. This program is -not- in the public domain. */

#import "GLUTMenuItem.h"
#import "GLUTMenu.h"


@implementation GLUTMenuItem

- (id)initWithTitle: (NSString *)title tag: (int)tag
{
   if((self = [self init]) != nil) {
      _title = [title copy];
      if(!_title) {
         [self release];
         return nil;
      }
      _tag = tag;
      _isTrigger = NO;

      return self;
   }
   return nil;
}

- (id)initWithTitle: (NSString *)title menu: (GLUTMenu *)menu
{
   if((self = [self init]) != nil) {
      _title = [title copy];
      if(!_title) {
         [self release];
         return nil;
      }
      _submenu = menu;
      _tag = 0;
      _isTrigger = YES;

      return self;
   }
   return nil;
}

- (void)dealloc
{
   [_title release];
   [super dealloc];
}

- (void)finalize
{
   [super finalize];
}


/* Accessors */
- (NSString *)title
{
   return _title;
}

- (void)setTitle: (NSString *)title
{
   if(_title != title) {
      [_title release];
      _title = [title copy];
      if(!_title) {
         __glutFatalError("out of memory");
      }
   }
}

- (GLUTMenu *)menu
{
   return _submenu;
}

- (void)setMenu: (GLUTMenu *)menu
{
   _submenu = menu;
   _isTrigger = (menu != nil);
}

- (int)tag
{
   return _tag;
}

- (void)setTag: (int)tag
{
   _tag = tag;
}

- (BOOL)isTrigger
{
   return _isTrigger;
}

@end
```

[Next](GLUTPreferencesController.h.md)[Previous](GLUTMenuItem.h.md)

