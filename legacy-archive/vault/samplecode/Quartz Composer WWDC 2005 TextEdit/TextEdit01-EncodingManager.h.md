---
title: Quartz Composer WWDC 2005 TextEdit
apple_id: DTS10003654
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzComposer_WWDC_TextEdit/Listings/TextEdit_01_EncodingManager_h.html
archived_at: '2026-07-18T03:21:30.867705Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer WWDC 2005 TextEdit](Quartz%20Composer%20WWDC%202005%20TextEdit.md)


[Next](TextEdit01-EncodingManager.m.md)[Previous](TextEdit01-Editmain.m.md)

# TextEdit_01/EncodingManager.h

```objc
#import <Foundation/Foundation.h>

enum {
    NoStringEncoding = 0xFFFFFFFF
};


@interface EncodingPopUpButton : NSPopUpButton {
    NSStringEncoding defaultEncoding;
    BOOL hasDefaultEntry;
}
- (void)setEncoding:(NSStringEncoding)encoding defaultEntry:(BOOL)flag;
@end



@interface EncodingManager : NSObject {
    @private
    IBOutlet NSMatrix *encodingMatrix;
    NSArray *encodings;
}

/* There is just one instance...
*/
+ (EncodingManager *)sharedInstance;

/* List of encodings that should be shown in encoding lists
*/
- (NSArray *)enabledEncodings;

/* Empties then initializes the supplied popup with the supported encodings.
*/
- (void)setupPopUp:(EncodingPopUpButton *)button selectedEncoding:(unsigned)selectedEncoding withDefaultEntry:(BOOL)flag;

/* Action methods for bringing up and dealing with changes in the encodings list panel
*/
- (IBAction)showPanel:(id)sender;
- (IBAction)encodingListChanged:(id)sender;
- (IBAction)clearAll:(id)sender;
- (IBAction)selectAll:(id)sender;
- (IBAction)revertToDefault:(id)sender;

/* Internal method to save and communicate changes to the encoding list
*/
- (void)noteEncodingListChange:(BOOL)writeDefault updateList:(BOOL)updateList postNotification:(BOOL)post;


@end
```

[Next](TextEdit01-EncodingManager.m.md)[Previous](TextEdit01-Editmain.m.md)

