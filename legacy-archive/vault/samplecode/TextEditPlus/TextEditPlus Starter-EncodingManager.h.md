---
title: TextEditPlus
apple_id: DTS10004025
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-28'
source_url: https://developer.apple.com/library/archive/samplecode/TextEditPlus/Listings/TextEditPlus_Starter_EncodingManager_h.html
archived_at: '2026-07-18T03:26:32.383170Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextEditPlus](TextEditPlus.md)


[Next](TextEditPlus%20Starter-EncodingManager.m.md)[Previous](TextEditPlus%20Starter-Editmain.m.md)

# TextEditPlus Starter/EncodingManager.h

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

[Next](TextEditPlus%20Starter-EncodingManager.m.md)[Previous](TextEditPlus%20Starter-Editmain.m.md)

