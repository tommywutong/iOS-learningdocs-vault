---
title: Calculator
apple_id: DTS10000560
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Calculator/Listings/CalcController_m.html
archived_at: '2026-07-18T03:02:48.723118Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [计算器](Calculator.md)


[Next](Calculatormain.m.md)[Previous](CalcController.h.md)

# CalcController.m

```objc
/*
File:       CalcController.m

Author:     AW, ES, and MCF

Copyright:  © Copyright 2000 Apple Computer, Inc. All rights reserved.

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc.
                ("Apple") in consideration of your agreement to the following terms, and your
                use, installation, modification or redistribution of this Apple software
                constitutes acceptance of these terms.  If you do not agree with these terms,
                please do not use, install, modify or redistribute this Apple software.

                In consideration of your agreement to abide by the following terms, and subject
                to these terms, Apple grants you a personal, non-exclusive license, under AppleÕs
                copyrights in this original Apple software (the "Apple Software"), to use,
                reproduce, modify and redistribute the Apple Software, with or without
                modifications, in source and/or binary forms; provided that if you redistribute
                the Apple Software in its entirety and without modifications, you must retain
                this notice and the following text and disclaimers in all such redistributions of
                the Apple Software.  Neither the name, trademarks, service marks or logos of
                Apple Computer, Inc. may be used to endorse or promote products derived from the
                Apple Software without specific prior written permission from Apple.  Except as
                expressly stated in this notice, no other rights or licenses, express or implied,
                are granted by Apple herein, including but not limited to any patent rights that
                may be infringed by your derivative works or by other works in which the Apple
                Software may be incorporated.

                The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
                WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
                WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR
                PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE OR IN
                COMBINATION WITH YOUR PRODUCTS.

                IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
                CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
                GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
                ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION
                OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT
                (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN
                ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

修改历史（最新的在前）：

9 July 97 -- 应用程序首个版本
7/5/00  KG  针对 DP4 上的 Project Builder 更新
12/04/00 MCF    针对 Mac OS X Public Beta 上的 Project Builder 更新

*/

#import "CalcController.h"

@implementation CalcController

// 此方法清空计算器的显示内容以及上一次运算的信息等
- (void)clear:(id)sender
{
    // 我们必须先 autorelease 旧对象，再 retain 新对象，这样才不会泄漏内存。
    [displayedNumber autorelease];
    displayedNumber = [[NSDecimalNumber zero] retain];
    [enteredNumber autorelease];
    enteredNumber = [[NSDecimalNumber zero] retain];
    [displayView setDoubleValue: 0];
    [self endEditingNumber];
    lastOperation = kNoOperator;
    usedDecimalPoint = NO;
}

- (void)equals:(id)sender
{
    if (enteringNumber)
      {
        [self endEditingNumber];
        [self performLastOperation];
        lastOperation = kNoOperator;
        [displayView setStringValue: [displayedNumber stringValue]];
      }
}

// 点击计算器上的数字按钮时会调用此方法
- (void)insertDigit:(id)sender
{
    NSString* oldValue;

    if (!enteringNumber)
      {
        [self beginEditingNumber];
      }


    oldValue = [displayView stringValue];
    [displayView setStringValue: [oldValue stringByAppendingString: [sender title]]];
}

- (void)beginEditingNumber
{
    enteringNumber = YES;
    usedDecimalPoint = NO;
    [displayView setStringValue: @""];
    [enteredNumber autorelease];
    enteredNumber = [displayedNumber copy]; 
}

- (void)endEditingNumber
{
    enteringNumber = NO;
    usedDecimalPoint = NO;

    [displayedNumber autorelease];
    displayedNumber = [NSDecimalNumber decimalNumberWithString: [displayView stringValue]];
    [displayedNumber retain];
}

- (void)decimalPoint:(id)sender
{
    NSString* oldValue;

    if (!usedDecimalPoint)
      {
        usedDecimalPoint = YES;
        if (!enteringNumber)
          {
            [self beginEditingNumber];
            [displayView setStringValue: @"0."];
          }
        else
          {
            oldValue = [displayView stringValue];
            [displayView setStringValue: [oldValue stringByAppendingString: @"."]];
          }
      }
}

// 应用程序首次启动并从 nib 文件实例化此对象时
// 会调用此方法
-(void) awakeFromNib
{
    [self clear: self];
    // 下一行是针对 Mac OS X Public Beta 中一个 bug 的变通处理
    [[displayView window] makeKeyAndOrderFront:nil];
}

- (void)operation:(id)sender
{
    if (enteringNumber)
      {
        [self endEditingNumber];
        [self performLastOperation];
        [displayView setStringValue: [displayedNumber stringValue]];
      }
    // 无论如何都设置新的运算操作，以防用户改变主意
    lastOperation = [sender tag];

}

- (void)performLastOperation
{
    if (lastOperation == kNoOperator)
      {
        return;
      }

    // 下面的代码其实可以大幅改写。在所有情况下，displayedNumber 都是先被
    // autorelease，然后赋予新值，再 retain 新值。因此，如果把 autorelease
    // 语句放到 if 语句嵌套块之前、把 retain 语句放到嵌套块之后，就能减少
    // 代码行数。然而，我特意重复了这些语句，就是为了直白地强调这一点：
    // 在给实例变量赋新值之前必须先 autorelease，赋值之后必须 retain。
    // 即使在没有任何一个 if 语句被执行的情况下，对同一个对象先 autorelease
    // 再立即 retain 也是完全可以接受的。

    // 这种检测 NaN 的方法是个 HACK！不幸的是，NaN 是无序的，所以如果你
    // 问任何一个数它是否等于 NaN，它都会回答"是"。因此，我们改为问它
    // 是否等于一个不可能的组合——零和一。唯一同时等于这两者的"数"就是 NaN
    if ((([displayedNumber compare: [NSDecimalNumber zero]] == NSOrderedSame) &&
         ([displayedNumber compare: [NSDecimalNumber one]] == NSOrderedSame)) ||
        (([enteredNumber compare: [NSDecimalNumber zero]] == NSOrderedSame) &&
         ([enteredNumber compare: [NSDecimalNumber one]] == NSOrderedSame)))
      {
        [displayedNumber autorelease];
        displayedNumber = [[NSDecimalNumber notANumber] retain];
        return;
      }
    else if (lastOperation == kAddOperator)
      {
        [displayedNumber autorelease];
       displayedNumber = [enteredNumber decimalNumberByAdding: displayedNumber];
        [displayedNumber retain];
      }
    else if (lastOperation == kSubtractOperator)
      {
        [displayedNumber autorelease];
        displayedNumber = [enteredNumber decimalNumberBySubtracting: displayedNumber];
        [displayedNumber retain];
      }
    else if (lastOperation == kMultiplyOperator)
      {
        [displayedNumber autorelease];
        displayedNumber = [enteredNumber decimalNumberByMultiplyingBy: displayedNumber];
        [displayedNumber retain];
      }
    else if (lastOperation == kDivideOperator)
      {
        if ([displayedNumber compare: [NSDecimalNumber zero]] != NSOrderedSame)
          {
            [displayedNumber autorelease];
            displayedNumber = [enteredNumber decimalNumberByDividingBy: displayedNumber];
            [displayedNumber retain];
          }
        else
          {
            [displayedNumber autorelease];
            displayedNumber = [[NSDecimalNumber notANumber] retain];
            [displayedNumber retain];
          }
      }
}

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)theApplication
{
    return YES;
}

- (void)cut:(id)sender
{
    [self copy: self];
    [self clear: self];
}

- (void)copy:(id)sender
{
    // 获取通用剪贴板
    NSPasteboard* pasteboard = [NSPasteboard generalPasteboard];
    // 告诉拷贝/粘贴系统我们将要放入的数据类型
    [pasteboard declareTypes: [NSArray arrayWithObject: NSStringPboardType] owner: NULL];
    // 把显示字符串放到剪贴板上，供其他应用粘贴
    [pasteboard setString: [displayView stringValue] forType: NSStringPboardType];
}

- (void)paste:(id)sender
{
    NSPasteboard* pasteboard;
    NSString* pasteValue;

    if (!enteringNumber)
      {
        [self beginEditingNumber];
      }
    // 获取通用剪贴板
    pasteboard = [NSPasteboard generalPasteboard];
    // 从剪贴板获取我们所需数据类型的内容
    pasteValue = [pasteboard stringForType: NSStringPboardType];
    // 设置计算器的显示内容
    [displayView setStringValue: [[displayView stringValue] stringByAppendingString: pasteValue]];
}

// 当 self 被释放时，必须释放所有我们 retain 过的变量
-(void)dealloc
{
    [displayedNumber release];
    [enteredNumber release];
}

@end
```

[Next](Calculatormain.m.md)[Previous](CalcController.h.md)
