---
title: Text Programming Guide for iOS
apple_id: TP40009542
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/LowerLevelText-HandlingTechnologies/LowerLevelText-HandlingTechnologies.html
archived_at: '2026-07-18T02:06:58.485557Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Programming Guide for iOS](About%20Text%20Handling%20in%20iOS.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Text%20Kit%20to%20Draw%20and%20Manage%20Text.md)

# Lower Level Text-Handling Technologies

Most apps can use the high-level text display classes and Text Kit for all their text handling. You might have an app, however, that requires the lower level programmatic interfaces from the Core Text, Core Graphics, and Core Animation frameworks as well as other APIs in UIKit itself.

In addition to the UIKit classes for displaying and editing text, iOS also includes several ways to draw text directly on the screen. The easiest and most efficient way to draw simple strings is using the UIKit additions to the [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) class, which is in a [category](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5) named `UIStringDrawing`. These extensions include methods for drawing strings using a variety of attributes wherever you want them on the screen. There are also methods for computing the size of a rendered string before you actually draw it, which can help you lay out your app content more precisely.

The methods of `UIStringDrawing` draw strings at a given point (for single lines of text) or within a specified rectangle (for multiple lines). You can pass in [attributes](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectModeling.html#//apple_ref/doc/uid/TP40008195-CH41) used in drawing—for example, font, line-break mode, and baseline adjustment. The methods of `UIStringDrawing` allow you to adjust the position of the rendered text precisely and blend it with the rest of your view’s content. They also let you compute the bounding rectangle for your text in advance based on the desired font and style attributes.

You can also use the [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer) class of Core Animation to do simple text drawing. An object of this class stores a plain string or attributed string as its content and offers a set of attributes that affect that content, such as font, font size, text color, and truncation behavior. The advantage of `CATextLayer` is that (being a subclass of [CALayer](https://developer.apple.com/documentation/quartzcore/calayer)) its [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) are inherently capable of animation. Core Animation is associated with the QuartzCore framework. Because instances of `CATextLayer` know how to draw themselves in the current [graphics context](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/DrawingModel.html#//apple_ref/doc/uid/TP40009071-CH9), you don’t need to issue any explicit drawing commands when using those instances.

For information about the string-drawing extensions to [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString), see _NSString UIKit Additions Reference_. To learn more about `CATextLayer`, `CALayer`, and the other classes of Core Animation, read _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.

Core Text is a technology for custom text layout and font management. App developers typically have no need to use Core Text directly. Text Kit is built on top of Core Text, giving it the same advantages, such as speed and sophisticated typographic capability. In addition, Text Kit provides a great deal of infrastructure that you must build for yourself if you use Core Text.

However, the Core Text API is accessible to developers who must use it directly. It is intended to be used by apps that have their own layout engines—for example, a word processor that has its own page layout engine can use Core Text to generate the glyphs and position them relative to each other.

Core Text is implemented as a [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) that publishes an API similar to that of Core Foundation—similar in that it is procedural (ANSI C) but is based on object-like opaque types. This API is integrated with both Core Foundation and Core Graphics. For example, Core Text uses Core Foundation and Core Graphics objects in many input and output parameters. Moreover, because many Core Foundation objects are “toll-free bridged” with their counterparts in the Foundation framework, you may use some Foundation objects in the parameters of Core Text functions.

Core Text has two major parts: a layout engine and font technology, each backed by its own collection of opaque types.

Core Text requires two objects whose opaque types are not native to it: an attributed string ([CFAttributedStringRef](https://developer.apple.com/documentation/corefoundation/cfattributedstringref)) and a graphics path ([CGPathRef](https://developer.apple.com/documentation/coregraphics/cgpath)). An attributed-string object encapsulates a string backing the displayed text and includes [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) (or, “attributes”) that define stylistic aspects of the characters in the string—for example, font and color. The graphics path defines the shape of a frame of text, which is equivalent to a paragraph.

Core Text objects at runtime form a hierarchy that is reflective of the level of the text being processed (see [Figure 9-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvonq)). At the top of this hierarchy is the framesetter object ([CTFramesetterRef](https://developer.apple.com/documentation/coretext/ctframesetterref)). With an attributed string and a graphics path as input, a framesetter generates one or more frames of text ([CTFrameRef](https://developer.apple.com/documentation/coretext/ctframeref)). As the text is laid out in a frame, the framesetter applies paragraph styles to it, including such attributes as alignment, tab stops, line spacing, indentation, and line-breaking mode.

To generate frames, the framesetter calls a typesetter object ([CTTypesetterRef](https://developer.apple.com/documentation/coretext/cttypesetterref)). The typesetter converts the characters in the attributed string to glyphs and fits those glyphs into the lines that fill a text frame. (A glyph is a graphic shape used to represent a character.) A line in a frame is represented by a `CTLine` object ([CTLineRef](https://developer.apple.com/documentation/coretext/ctlineref)). A `CTFrame` object contains an array of `CTLine` objects.

A `CTLine` object, in turn, contains an array of glyph runs, represented by objects of the [CTRunRef](https://developer.apple.com/documentation/coretext/ctrun) type. A glyph run is a series of consecutive glyphs that have the same attributes and direction. Although a typesetter object returns `CTLine` objects, it composes those lines from arrays of glyph runs.

__Figure 9-1__  Core Text layout objects

!

Using functions of the `CTLine` opaque type, you can draw a line of text from an attributed string without having to go through the `CTFramesetter` object. You simply position the origin of the text on the text baseline and request the line object to draw itself.

Fonts are essential to text processing in Core Text. The typesetter object uses fonts (along with the source attributed string) to convert glyphs from characters and then position those glyphs relative to one another. A [graphics context](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/DrawingModel.html#//apple_ref/doc/uid/TP40009071-CH9) is central to fonts in Core Text. You can use graphics-context functions to set the current font and draw glyphs; or you can create a `CTLine` object from an attributed string and use its functions to draw into the graphics context. The Core Text font system handles Unicode fonts natively.

The font system includes objects of three opaque types: `CTFont`, `CTFontDescriptor`, and `CTFontCollection`:

- Font objects ([CTFontRef](https://developer.apple.com/documentation/coretext/ctfontref)) are initialized with a point size and specific characteristics (from a transformation matrix). You can query the font object for its character-to-glyph mapping, its encoding, glyph data, and metrics such as ascent, leading, and so on. Core Text also offers an automatic font-substitution mechanism called font cascading.
- Font descriptor objects ([CTFontDescriptorRef](https://developer.apple.com/documentation/coretext/ctfontdescriptor)) are typically used to create font objects. Instead of dealing with a complex transformation matrix, they allow you to specify a dictionary of font attributes that include such properties as PostScript name, font family and style, and traits (for example, bold or italic).
- Font collection objects ([CTFontCollectionRef](https://developer.apple.com/documentation/coretext/ctfontcollection)) are groups of font descriptors that provide services such as font enumeration and access to global and custom font collections.

It’s possible to convert [UIFont](https://developer.apple.com/documentation/uikit/uifont) objects to `CTFont` objects by calling [CTFontCreateWithName](https://developer.apple.com/documentation/coretext/1509153-ctfontcreatewithname), passing the font name and point size encapsulated by the `UIFont` object.

Core Graphics (or Quartz) is the system [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) that handles two-dimensional imaging at the lowest level. Text drawing is one of its capabilities. Generally, because Core Graphics is so low-level, it is recommended that you use one of the system’s other technologies for drawing text. However, if circumstances require it, you can draw text with Core Graphics.

You select fonts, set text attributes, and draw text using functions of the CGContext opaque type. For example, you can call [CGContextSelectFont](https://developer.apple.com/documentation/coregraphics/cgcontext/1586511-selectfont) to set the font used, and then call [CGContextSetFillColor](https://developer.apple.com/documentation/coregraphics/1455296-cgcontextsetfillcolor) to set the text color. You then set the text matrix ([CGContextSetTextMatrix](https://developer.apple.com/documentation/coregraphics/1455611-cgcontextsettextmatrix)) and draw the text using [CGContextShowGlyphsAtPoint](https://developer.apple.com/documentation/coregraphics/cgcontext/1586502-showglyphsatpoint).

For more information about these functions and their use, see _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_ and _Core Graphics Framework Reference_.

The [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) class of the Foundation framework includes a simple programmatic interface for regular expressions. You call one of three methods that return a range, passing in a specific option constant and a regular-expression string. If there is a match, the method returns the range of the substring. The option is the [NSRegularExpressionSearch](https://developer.apple.com/documentation/foundation/nsstring/compareoptions/1410450-regularexpression) constant, which is of bit-mask type [NSStringCompareOptions](https://developer.apple.com/documentation/foundation/nsstringcompareoptions); this constant tells the method to expect a regular-expression pattern rather than a literal string as the search value. The supported regular expression syntax is that defined by ICU (International Components for Unicode).

The `NSString` methods for regular expressions are the following:

- [rangeOfString:options:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:)
- [rangeOfString:options:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:range:)
- [rangeOfString:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1417348-range)

If you specify the `NSRegularExpressionSearch` option in these methods, the only other [NSStringCompareOptions](https://developer.apple.com/documentation/foundation/nsstringcompareoptions) options you may specify are [NSCaseInsensitiveSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSCaseInsensitiveSearch) and [NSAnchoredSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSAnchoredSearch). If a regular-expression search does not find a match or the regular-expression syntax is malformed, these methods return an [NSRange](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRange) structure with a value of `{NSNotFound, 0}`.

Listing 9-1 gives an example of using the `NSString` regular-expression API.

__Listing 9-1__  Finding a substring using a regular expression

```
    // finds phone number in format nnn-nnn-nnnn
    NSRange r;
    NSString *regEx = @"[0-9]{3}-[0-9]{3}-[0-9]{4}";
    r = [textView.text rangeOfString:regEx options:NSRegularExpressionSearch];
    if (r.location != NSNotFound) {
        NSLog(@"Phone number is %@", [textView.text substringWithRange:r]);
    } else {
        NSLog(@"Not found.");
    }
```

Because these methods return a single range value for the substring matching the pattern, certain regular-expression capabilities of the ICU library are either not available or have to be programmatically added. In addition, `NSStringCompareOptions` options such as backward search, numeric search, and diacritic-insensitive search are not available and capture groups are not supported.

When testing the returned range, you should be aware of certain behavioral differences between searches based on literal strings and searches based on regular-expression patterns. Some patterns can successfully match and return an [NSRange](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRange) structure with a `length` of 0 (in which case the `location` field is of interest). Other patterns can successfully match against an empty string or, in those methods with a range parameter, with a zero-length search range.

In case the `NSString` support for regular expressions is not sufficient for your needs, a modified version of the libraries from ICU 4.2.1 is included in iOS at the BSD (nonframework) level of the system. ICU (International Components for Unicode) is an open-source project for Unicode support and software internationalization. The installed version of ICU includes those header files necessary to support regular expressions, along with some modifications related to those interfaces, namely:

- `parseerr.h`
- `platform.h`
- `putil.h`
- `uconfig.h`
- `udraft.h`
- `uintrnal.h`
- `uiter.h`
- `umachine.h`
- `uregex.h`
- `urename.h`
- `ustring.h`
- `utf_old.h`
- `utf.h`
- `utf16.h`
- `utf8.h`
- `utypes.h`
- `uversion.h`

You can read the ICU 4.2 API documentation and user guide at [http://icu-project.org/apiref/icu4c/index.html](http://icu-project.org/apiref/icu4c/index.html).

An app that wants to display and process text is not limited to the text and web objects of the UIKit [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56). It can implement [custom views](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/ViewObject.html#//apple_ref/doc/uid/TP40009071-CH5) that are capable of anything from simple text entry to complex text processing and custom input. Through the available programming interfaces, these apps can acquire features such as custom text layout, multistage input, autocorrection, custom keyboards, and spell-checking.

You can implement custom views that allow users to enter text at an insertion point and delete characters before that insertion point when they tap the Delete key. An instant-messaging app, for example, could have a view that allows users to enter their part of a conversation.

You can acquire this capability for simple text entry by subclassing [UIView](https://developer.apple.com/documentation/uikit/uiview), or any other view class that inherits from `UIResponder`, and adopting the [UIKeyInput](https://developer.apple.com/documentation/uikit/uikeyinput) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45). When an instance of your view class becomes the first responder, UIKit displays the system keyboard. `UIKeyInput` itself adopts the [UITextInputTraits](https://developer.apple.com/documentation/uikit/uitextinputtraits) protocol, so you can set keyboard type, return-key type, and other attributes of the keyboard.

To adopt `UIKeyInput`, you must implement the three methods it declares: [hasText](https://developer.apple.com/documentation/uikit/uikeyinput/1614457-hastext), [insertText:](https://developer.apple.com/documentation/uikit/uikeyinput/1614543-inserttext), and [deleteBackward](https://developer.apple.com/documentation/uikit/uikeyinput/1614572-deletebackward). To do the actual drawing of the text, you may use any of the technologies summarized in this chapter. However, for simple text input, such as for a single line of text in a custom [control](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Control.html#//apple_ref/doc/uid/TP40009071-CH7), the `UIStringDrawing` and `CATextLayer` APIs are most appropriate.

Listing 9-2 illustrates the `UIKeyInput` implementation of a custom view class. The `textStore` property in this example is an [NSMutableString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSMutableString) object that serves as the backing store of text. The implementation either appends or removes the last character in the string (depending on whether an alphanumeric key or the Delete key is pressed) and then redraws `textStore`.

__Listing 9-2__  Implementing simple text entry

```objc
- (BOOL)hasText {
    if (textStore.length > 0) {
        return YES;
    }
    return NO;
}

- (void)insertText:(NSString *)theText {
    [self.textStore appendString:theText];
    [self setNeedsDisplay];
}

- (void)deleteBackward {
    NSRange theRange = NSMakeRange(self.textStore.length-1, 1);
    [self.textStore deleteCharactersInRange:theRange];
    [self setNeedsDisplay];
}

- (void)drawRect:(CGRect)rect {
    CGRect rectForText = [self rectForTextWithInset:2.0]; // custom method
    [self.theColor set];
    UIRectFrame(rect);
    [self.textStore drawInRect:rectForText withFont:self.theFont];
}
```

To actually draw the text in the view, this code uses the [drawInRect:withFont:](https://developer.apple.com/documentation/foundation/nsstring/1619909-drawinrect) from the `UIStringDrawing` category on [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString).

The text input system of iOS manages the keyboard. It interprets taps as presses of specific keys in specific keyboards suitable for certain languages. It then sends the associated character to the target view for insertion. As explained in [Simple Text Input](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvomjt), view classes must adopt the [UIKeyInput](https://developer.apple.com/documentation/uikit/uikeyinput)[protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) to insert and delete characters at the caret (insertion point).

However, the text input system does more than simple text entry. For example, it manages autocorrection and multistage input, which are all based upon the current selection and context. Multistage text input is required for ideographic languages such as Kanji (Japanese) and Hanzi (Chinese), which take input from phonetic keyboards. To acquire these features, a custom text view must communicate with the text input system by adopting the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol and implementing the related client-side classes and protocols.

The following section describes the general responsibilities of a custom text view that communicates with the text input system. [A Guided Tour of a UITextInput Implementation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvomrt) examines the most important classes and methods of a typical implementation of `UITextInput`.

A class that wants to communicate with the text input system must adopt the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol. The class needs to inherit from [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) and is in most cases a custom [view](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/ViewObject.html#//apple_ref/doc/uid/TP40009071-CH5).

The text view must do its own text layout and font management; for this purpose, the Core Text framework is recommended. ([Core Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvomy) gives an overview of Core Text.) The class should also adopt and implement the `UIKeyInput` protocol and should set the necessary properties of the [UITextInputTraits](https://developer.apple.com/documentation/uikit/uitextinputtraits) protocol.

The general architecture of the client and system sides of the text input system are diagrammed in Figure 9-2.

__Figure 9-2__  Paths of communication with the text input system

!

The text input system calls the `UITextInput` methods that the text view implements. Many of these methods request information about specific text positions and text ranges from the text view and pass the same information back to the class in other method calls. The reasons for these exchanges of text positions and text ranges are summarized in [Tasks of a UITextInput Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvomrr).

Text positions and text ranges in the text input system are represented by instances of custom classes. [Text Positions and Text Ranges](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvomrq) discusses these objects in more detail.

The text view also maintains references to a tokenizer and an input [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14). The text view calls methods declared by the [UITextInputDelegate](https://developer.apple.com/documentation/uikit/uitextinputdelegate) protocol to notify a system-provided input delegate about external changes in text and selection. The text input system communicates with a tokenizer object to determine the granularity of text units—for example, character, word, and paragraph. The tokenizer is an object that adopts the [UITextInputTokenizer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer) protocol. The text view includes a property (declared by `UITextInput`) that holds a reference to the tokenizer.

The client app must create two classes whose instances represent positions and ranges of text in a text view. These classes must be subclasses of [UITextPosition](https://developer.apple.com/documentation/uikit/uitextposition) and [UITextRange](https://developer.apple.com/documentation/uikit/uitextrange).

Although `UITextPosition` itself declares no methods or properties, it is an essential part of the information exchanged between a text document and the text input system. The text input system requires an object to represent a location in the text instead of, say, an integer or a structure. Moreover, a `UITextPosition` object can serve a practical purpose by representing a position in the visible text when the string backing the text has a different offset to that position. This happens when the string contains invisible formatting characters, such as with RTF and HTML documents, or embedded objects, such as an attachment. The custom `UITextPosition` class can account for these invisible characters when locating the string offsets of visible characters. In the simplest case—a plain text document with no embedded objects—a custom `UITextPosition` object can encapsulate a single offset or index integer.

`UITextRange` declares a simple interface in which two of its properties are starting and ending custom `UITextPosition` objects. The third property holds a Boolean value that indicates whether the range is empty (that is, has no length).

A class adopting the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) is required to implement most of the protocol’s methods and [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13). With a few exceptions, these methods take custom [UITextPosition](https://developer.apple.com/documentation/uikit/uitextposition) or [UITextRange](https://developer.apple.com/documentation/uikit/uitextrange) objects as parameters or return one of these objects. At runtime the text system invokes these methods and, again in almost all cases, expects some object or value back.

The text view must assign text positions to properties marking the beginning and end of the displayed text. In addition, it must also maintain the range of the currently selected text and the range of the currently marked text, if any. Marked text, which is part of multistage text input, represents provisionally inserted text the user has yet to confirm. It is styled in a distinctive way. The range of marked text always contains within it a range of selected text, which might be a range of characters or the caret.

The methods implemented by a `UITextInput` object can be divided into distinctive tasks:

- _Returning and replacing text by text range._ Given a range, either return the text in that range or replace that text with text provided by the text input system.

  - [textInRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614527-textinrange)
  - [replaceRange:withText:](https://developer.apple.com/documentation/uikit/uitextinput/1614558-replacerange)
- _Computing text ranges and text positions._[Create](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) and return a `UITextRange` object (or, simply, a text range) given two text positions; or create and return a `UITextPosition` object (or, simply, a text position) given a text position and an offset.

  - [positionFromPosition:offset:](https://developer.apple.com/documentation/uikit/uitextinput/1614511-positionfromposition)
  - [positionFromPosition:inDirection:offset:](https://developer.apple.com/documentation/uikit/uitextinput/1614515-positionfromposition)
  - [textRangeFromPosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614573-textrangefromposition)
- _Evaluating text positions._ Compare two text positions or return the offset from one text position to another.

  - [comparePosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614526-compareposition)
  - [offsetFromPosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614473-offsetfromposition)
- _Answering layout questions._ Determine a text position or text range by extending in a given layout direction.

  - [positionWithinRange:farthestInDirection:](https://developer.apple.com/documentation/uikit/uitextinput/1614547-position)
  - [characterRangeByExtendingPosition:inDirection:](https://developer.apple.com/documentation/uikit/uitextinput/1614462-characterrangebyextendingpositio)
- _Hit-testing._ Given a point, return the closest text position or text range.

  - [closestPositionToPoint:](https://developer.apple.com/documentation/uikit/uitextinput/1614523-closestpositiontopoint)
  - [closestPositionToPoint:withinRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614533-closestpositiontopoint)
  - [characterRangeAtPoint:](https://developer.apple.com/documentation/uikit/uitextinput/1614574-characterrange)
- _Returning rectangles for text ranges and text positions._ Return the rectangle that encloses a text range or the rectangle at the text position of the caret.

  - [firstRectForRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614570-firstrectforrange)
  - [caretRectForPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614518-caretrectforposition)

The `UITextInput` object might also choose to implement one or more optional protocol methods. These enable it to return text styles (font, text color, background color) beginning at a specified text position and to reconcile visible text position and character offset (for those `UITextPosition` objects where these values are not the same).

When changes occur in the text view due to external reasons—that is, they aren't caused by calls from the text input system—the `UITextInput` object should send [textWillChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614520-textwillchange), [textDidChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614499-textdidchange), [selectionWillChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614540-selectionwillchange), and [selectionDidChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614551-selectiondidchange) messages to the input delegate (which it holds a reference to). For example, when users tap a text view and you set the range of selected text to place the insertion point under the finger, you would send [selectionWillChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614540-selectionwillchange) before you change the selected range, and you send [selectionDidChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614551-selectiondidchange) after you change the range.

Tokenizers are objects that determine whether a text position is within or at the boundary of a text unit with a given granularity. When queried by the text input system, a tokenizer returns ranges of text units with a given granularity or the boundary text position for a text unit with a given granularity. Currently defined granularities are character, word, sentence, paragraph, line, and document; `enum` constants of the [UITextGranularity](https://developer.apple.com/documentation/uikit/uitextgranularity) type represent these granularities. Granularities of text units are always evaluated with reference to a storage or layout direction.

The text input system uses the tokenizer in a variety of ways. For example, the keyboard might require the last sentence’s worth of context to figure out what the user is trying to type. Or, if the user is pressing the Option-left arrow key (on an external keyboard), the text system queries the tokenizer to find the information it needs to move to the previous word.

A tokenizer is an instance of a class that conforms to the [UITextInputTokenizer](https://developer.apple.com/documentation/uikit/uitextinputtokenizer) [protocol](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45). The [UITextInputStringTokenizer](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer) class provides a default base implementation of the `UITextInputTokenizer` protocol that is suitable for all supported languages. If you require a tokenizer with an entirely new interpretation of text units of varying granularity, you should adopt `UITextInputTokenizer` and implement all of its methods. Otherwise you should subclass `UITextInputStringTokenizer` to provide app-specific information about layout directions.

When you [initialize](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) a `UITextInputStringTokenizer` object, you supply it with the view adopting the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol. In turn, the `UITextInput` object should lazily create its tokenizer object in the [getter method](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) of the tokenizer property.

_[SimpleTextInput](../../../samplecode/SimpleTextInput/SimpleTextInput.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytanrtgm)_ is a simple text-editing app based on Core Text. It has two custom subclasses of [UIView](https://developer.apple.com/documentation/uikit/uiview). One view subclass, `SimpleCoreTextView`, provides text layout and editing support using Core Text. The other view subclass, `EditableCoreTextView`, adopts the [UIKeyInput](https://developer.apple.com/documentation/uikit/uikeyinput) protocol to enable text input; it also adopts the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol and creates and implements the related subclasses to communicate with the text input system. `EditableCoreTextView` embeds `SimpleCoreTextView` as an instance variable, instantiates it, and calls through to it in most `UITextInput` and `UIKeyInput` method implementations.

`EditableCoreTextView` creates a custom subclass of [UITextPosition](https://developer.apple.com/documentation/uikit/uitextposition) called `IndexedPosition` and a custom subclass of [UITextRange](https://developer.apple.com/documentation/uikit/uitextrange) called `IndexedRange`. These subclasses simply encapsulate a single index value and an [NSRange](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSRange) value based on two of those indexes. Listing 9-3 shows the declaration of these classes.

__Listing 9-3__  Declaring the `IndexedPosition` and `IndexedRange` classes

```objc
@interface IndexedPosition : UITextPosition {
    NSUInteger _index;
    id <UITextInputDelegate> _inputDelegate;
}
@property (nonatomic) NSUInteger index;
+ (IndexedPosition *)positionWithIndex:(NSUInteger)index;
@end

@interface IndexedRange : UITextRange {
    NSRange _range;
}
@property (nonatomic) NSRange range;
+ (IndexedRange *)rangeWithNSRange:(NSRange)range;

@end
```

Both classes declare class factory methods to vend instances. Listing 9-4 shows the implementation of these methods as well as the methods declared by the `UITextRange` class.

__Listing 9-4__  Implementing the `IndexedPosition` and `IndexedRange` classes

```objc
@implementation IndexedPosition
@synthesize index = _index;

+ (IndexedPosition *)positionWithIndex:(NSUInteger)index {
    IndexedPosition *pos = [[IndexedPosition alloc] init];
    pos.index = index;
    return [pos autorelease];
}

@end

@implementation IndexedRange
@synthesize range = _range;

+ (IndexedRange *)rangeWithNSRange:(NSRange)nsrange {
    if (nsrange.location == NSNotFound)
        return nil;
    IndexedRange *range = [[IndexedRange alloc] init];
    range.range = nsrange;
    return [range autorelease];
}

- (UITextPosition *)start {
    return [IndexedPosition positionWithIndex:self.range.location];
}

- (UITextPosition *)end {
        return [IndexedPosition positionWithIndex:(self.range.location + self.range.length)];
}

-(BOOL)isEmpty {
    return (self.range.length == 0);
}
@end
```


A text view that adopts the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol must also adopt the [UIKeyInput](https://developer.apple.com/documentation/uikit/uikeyinput) protocol. That means it must implement the [insertText:](https://developer.apple.com/documentation/uikit/uikeyinput/1614543-inserttext), [deleteBackward](https://developer.apple.com/documentation/uikit/uikeyinput/1614572-deletebackward), and [hasText](https://developer.apple.com/documentation/uikit/uikeyinput/1614457-hastext) methods as discussed in [Simple Text Input](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjvfvjvomjt). Because the `EditableCoreTextView` class is adopting `UITextInput`, it must also maintain the selected and marked text ranges (that is, the current values of the [selectedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614541-selectedtextrange) and [markedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614489-markedtextrange) properties) as text is entered and deleted.

Listing 9-5 illustrates how `EditableCoreTextView` does this when text is entered. If there is marked text when a character is entered, it replaces the marked text with the character by calling the `replaceCharactersInRange:withString:` method on the backing mutable string. If there is a selected range of text, it replaces the characters in that range with the input character. Otherwise, the method inserts the input character at the caret.

__Listing 9-5__  Inserting text input into storage and updating selected and marked ranges

```objc
- (void)insertText:(NSString *)text {
    NSRange selectedNSRange = _textView.selectedTextRange;
    NSRange markedTextRange = _textView.markedTextRange;

    if (markedTextRange.location != NSNotFound) {
        [_text replaceCharactersInRange:markedTextRange withString:text];
        selectedNSRange.location = markedTextRange.location + text.length;
        selectedNSRange.length = 0;
        markedTextRange = NSMakeRange(NSNotFound, 0);
    } else if (selectedNSRange.length > 0) {
        [_text replaceCharactersInRange:selectedNSRange withString:text];
        selectedNSRange.length = 0;
        selectedNSRange.location += text.length;
    } else {
        [_text insertString:text atIndex:selectedNSRange.location];
        selectedNSRange.location += text.length;
    }
    _textView.text = _text;
    _textView.markedTextRange = markedTextRange;
    _textView.selectedTextRange = selectedNSRange;
}
```

Even though the structure of the [deleteBackward](https://developer.apple.com/documentation/uikit/uikeyinput/1614572-deletebackward) method implemented by `EditableCoreTextView` is identical to the `insertText:` method, there are appropriate differences in how the selected and marked text ranges are adjusted. Another difference is that the [deleteCharactersInRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/deleteCharactersInRange:) method is called on the backing mutable string rather than `replaceCharactersInRange:withString:`.

Any text view that communicates with the text input system must, when requested, return a specified range of text and replace a range of text with a given string. The classes in our example, `EditableCoreTextView` and `SimpleCoreTextView`, maintain synchronized copies of the backing string object (`EditableCoreTextView` as a [NSMutableString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSMutableString) object). The implementations of [textInRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614527-textinrange) and [replaceRange:withText:](https://developer.apple.com/documentation/uikit/uitextinput/1614558-replacerange) in Listing 9-6 call the appropriate `NSString` methods on the backing string to accomplish their essential functions.

__Listing 9-6__  Implementations of `textInRange:` and `replaceRange:withText:`

```objc
- (NSString *)textInRange:(UITextRange *)range
{
    IndexedRange *r = (IndexedRange *)range;
    return ([_text substringWithRange:r.range]);
}

- (void)replaceRange:(UITextRange *)range withText:(NSString *)text
{
    IndexedRange *r = (IndexedRange *)range;
    NSRange selectedNSRange = _textView.selectedTextRange;
    if ((r.range.location + r.range.length) <= selectedNSRange.location) {
        selectedNSRange.location -= (r.range.length - text.length);
    } else {
        // Need to also deal with overlapping ranges.
    }
    [_text replaceCharactersInRange:r.range withString:text];
    _textView.text = _text;
    _textView.selectedTextRange = selectedNSRange;
}
```

When the `text` property of `SimpleCoreTextView` changes (as shown in the implementation of `replaceRange:withText:`), `SimpleCoreTextView` lays out the text again and redraws it using Core Text functions.

Because editing operations are performed on selected and marked text, the text input system frequently requests that the text view return and set the ranges of selected and marked text. Listing 9-7 shows how `EditableCoreTextView` returns the ranges of selected and marked text by implementing [getter methods](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) for the [selectedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614541-selectedtextrange) and [markedTextRange](https://developer.apple.com/documentation/uikit/uitextinput/1614489-markedtextrange)[properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13).

__Listing 9-7__  Returning ranges of selected and marked text

```objc
- (UITextRange *)selectedTextRange {
    return [IndexedRange rangeWithNSRange:_textView.selectedTextRange];
}

- (UITextRange *)markedTextRange {
    return [IndexedRange rangeWithNSRange:_textView.markedTextRange];
}
```

The setter method for the `selectedTextRange` in Listing 9-8 simply sets the selected-text range on the embedded text view. The [setMarkedText:selectedRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614465-setmarkedtext) method is more complex because, as you may recall, the range of marked text contains within it the range of selected text (even if the range merely identifies the caret), and these ranges have to be reconciled to reflect the situation after the insertion of text.

__Listing 9-8__  Setting the range of selected text and setting the marked text

```objc
- (void)setSelectedTextRange:(UITextRange *)range
{
    IndexedRange *r = (IndexedRange *)range;
    _textView.selectedTextRange = r.range;
}

- (void)setMarkedText:(NSString *)markedText selectedRange:(NSRange)selectedRange {
    NSRange selectedNSRange = _textView.selectedTextRange;
    NSRange markedTextRange = _textView.markedTextRange;

    if (markedTextRange.location != NSNotFound) {
        if (!markedText)
            markedText = @"";
        [_text replaceCharactersInRange:markedTextRange withString:markedText];
        markedTextRange.length = markedText.length;
    } else if (selectedNSRange.length > 0) {
        [_text replaceCharactersInRange:selectedNSRange withString:markedText];
        markedTextRange.location = selectedNSRange.location;
        markedTextRange.length = markedText.length;
    } else {
        [_text insertString:markedText atIndex:selectedNSRange.location];
        markedTextRange.location = selectedNSRange.location;
        markedTextRange.length = markedText.length;
    }
    selectedNSRange = NSMakeRange(selectedRange.location + markedTextRange.location,
        selectedRange.length);

    _textView.text = _text;
    _textView.markedTextRange = markedTextRange;
    _textView.selectedTextRange = selectedNSRange;
}
```

Note that `EditableCoreTextView` replaces the text by calling the [replaceCharactersInRange:withString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/replaceCharactersInRange:withString:) method on its mutable string object, which it then assigns to the `text` property of the embedded text view.

When users type characters on the keyboard and when those characters enter text storage and are laid out, the text input system requests information from the object adopting the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol. Three of the more frequently called methods are [textRangeFromPosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614573-textrangefromposition), [offsetFromPosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614473-offsetfromposition), and [positionFromPosition:offset:](https://developer.apple.com/documentation/uikit/uitextinput/1614511-positionfromposition).

The text input system calls [positionFromPosition:offset:](https://developer.apple.com/documentation/uikit/uitextinput/1614511-positionfromposition) to get the position in the text that’s a given offset from another position. Listing 9-9 shows how `EditableCoreTextView` implements this method (which includes range checking).

__Listing 9-9__  Implementing `positionFromPosition:offset:`

```objc
- (UITextPosition *)positionFromPosition:(UITextPosition *)position offset:(NSInteger)offset {
    IndexedPosition *pos = (IndexedPosition *)position;
    NSInteger end = pos.index + offset;
    if (end > _text.length || end < 0)
        return nil;
    return [IndexedPosition positionWithIndex:end];
}
```

The [offsetFromPosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614473-offsetfromposition) method should satisfy the opposite request and return a value specifying the offset between two text positions. `EditableCoreTextView` implements it as shown in Listing 9-10.

__Listing 9-10__  Implementing `offsetFromPosition:toPosition:`

```objc
- (NSInteger)offsetFromPosition:(UITextPosition *)from toPosition:(UITextPosition *)toPosition {
    IndexedPosition *f = (IndexedPosition *)from;
    IndexedPosition *t = (IndexedPosition *)toPosition;
    return (t.index - f.index);
}
```

Finally, the text input system frequently asks a text view for a text range that falls between two text positions. Listing 9-11 shows an implementation of [textRangeFromPosition:toPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614573-textrangefromposition) that returns this range.

__Listing 9-11__  Implementing `textRangeFromPosition:toPosition:`

```objc
- (UITextRange *)textRangeFromPosition:(UITextPosition *)fromPosition
          toPosition:(UITextPosition *)toPosition {
    IndexedPosition *from = (IndexedPosition *)fromPosition;
    IndexedPosition *to = (IndexedPosition *)toPosition;
    NSRange range = NSMakeRange(MIN(from.index, to.index), ABS(to.index - from.index));
    return [IndexedRange rangeWithNSRange:range];
}
```


When a correction bubble appears and when the user types in Japanese, the text input system sends [firstRectForRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614570-firstrectforrange) and [caretRectForPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614518-caretrectforposition) to the text view. The purpose of both of these methods is to return a rectangle enclosing either a range of text or the caret that marks the insertion point. The `EditableCoreTextView` class implements the first of these methods by calling a method of its embedded text view that maps the range to an enclosing rectangle (see Listing 9-12). Before returning the rectangle, it converts it to the local coordinate system.

__Listing 9-12__  An implementation of `firstRectForRange:`

```objc
- (CGRect)firstRectForRange:(UITextRange *)range {
    IndexedRange *r = (IndexedRange *)range;
    CGRect rect = [_textView firstRectForNSRange:r.range];
    return [self convertRect:rect fromView:_textView];
}
```

The embedded text view in this case performs the lion’s share of the work. Using Core Text functions, it computes the rectangle that encloses the range of text and returns it, as shown in Listing 9-13.

__Listing 9-13__  Mapping text range to enclosing rectangle

```objc
- (CGRect)firstRectForNSRange:(NSRange)range; {
    int index = range.location;
    NSArray *lines = (NSArray *) CTFrameGetLines(_frame);
    for (int i = 0; i < [lines count]; i++) {
        CTLineRef line = (CTLineRef) [lines objectAtIndex:i];
        CFRange lineRange = CTLineGetStringRange(line);
        int localIndex = index - lineRange.location;
        if (localIndex >= 0 && localIndex < lineRange.length) {
            int finalIndex = MIN(lineRange.location + lineRange.length,
                range.location + range.length);
            CGFloat xStart = CTLineGetOffsetForStringIndex(line, index, NULL);
            CGFloat xEnd = CTLineGetOffsetForStringIndex(line, finalIndex, NULL);
            CGPoint origin;
            CTFrameGetLineOrigins(_frame, CFRangeMake(i, 0), &origin);
            CGFloat ascent, descent;
            CTLineGetTypographicBounds(line, &ascent, &descent, NULL);

            return CGRectMake(xStart, origin.y - descent, xEnd - xStart, ascent + descent);
        }
    }
    return CGRectNull;
}
```

For [caretRectForPosition:](https://developer.apple.com/documentation/uikit/uitextinput/1614518-caretrectforposition), the approach you take would be somewhat different. Selection affinity ([selectionAffinity](https://developer.apple.com/documentation/uikit/uitextinput/1614539-selectionaffinity)) is a factor to consider; more importantly, keep in mind that the height and width of the caret rectangle can be different from the bounding rectangle returned from [firstRectForRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614570-firstrectforrange).

Another area where the text input system asks the text view to map between the display of text and the storage of text is hit testing. Given a point in the text view (the text input system asks), what is the corresponding text position or text range? The `UITextInput` methods it calls for this information are [closestPositionToPoint:](https://developer.apple.com/documentation/uikit/uitextinput/1614523-closestpositiontopoint), [closestPositionToPoint:withinRange:](https://developer.apple.com/documentation/uikit/uitextinput/1614533-closestpositiontopoint), and [characterRangeAtPoint:](https://developer.apple.com/documentation/uikit/uitextinput/1614574-characterrange). Listing 9-14 illustrates how `EditableCoreTextView` implements the first of these methods.

__Listing 9-14__  An implementation of `closestPositionToPoint:`

```objc
- (UITextPosition *)closestPositionToPoint:(CGPoint)point {
    NSInteger index = [_textView closestIndexToPoint:point];
    return [IndexedPosition positionWithIndex:(NSUInteger)index];
}
```

Here, as with the methods that return rectangles for text ranges or text positions, `EditableCoreTextView` calls a method of its embedded view that uses Core Text to calculate the character index that corresponds to the point. Listing 9-15 illustrates how the embedded view accomplishes this.

__Listing 9-15__  Mapping a point to a character index

```objc
- (NSInteger)closestIndexToPoint:(CGPoint)point {
    NSArray *lines = (NSArray *) CTFrameGetLines(_frame);
    CGPoint origins[lines.count];
    CTFrameGetLineOrigins(_frame, CFRangeMake(0, lines.count), origins);

    for (int i = 0; i < lines.count; i++) {
        if (point.y > origins[i].y) {
            CTLineRef line = (CTLineRef) [lines objectAtIndex:i];
            return CTLineGetStringIndexForPosition(line, point);
        }
    }
    return  _text.length;
}
```


When there is a change in text or a change in selection that is not initiated by the text input system, you should inform the text input delegate by sending it an appropriate “will-change” method. After making the change, send the delegate the corresponding “did-change” method.

The text input delegate is a system-provided object that adopts the [UITextInputDelegate](https://developer.apple.com/documentation/uikit/uitextinputdelegate) protocol. If the class adopting the [UITextInput](https://developer.apple.com/documentation/uikit/uitextinput) protocol defines an [inputDelegate](https://developer.apple.com/documentation/uikit/uitextinput/1614508-inputdelegate) property, the text input system automatically assigns a delegate object to this property at runtime.

Listing 9-16 shows an action method that is invoked when the user taps in the text view. If the view is tapped but it isn’t the first responder, the text view makes itself the first responder and starts an editing session. If the view is subsequently tapped, the text view sends a [selectionWillChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614540-selectionwillchange) message to the text input delegate. It then clears any marked text range and resets the selected text range so that the caret is at the point in the text where the tapped occurred. After this, it calls [selectionDidChange:](https://developer.apple.com/documentation/uikit/uitextinputdelegate/1614551-selectiondidchange).

__Listing 9-16__  Sending messages to the text input delegate

```objc
- (void)tap:(UITapGestureRecognizer *)tap
{
    if (![self isFirstResponder]) {
        _textView.editing = YES;
        [self becomeFirstResponder];
    } else {
        [self.inputDelegate selectionWillChange:self];

        NSInteger index = [_textView closestIndexToPoint:[tap locationInView:_textView]];
        _textView.markedTextRange = NSMakeRange(NSNotFound, 0);
        _textView.selectedTextRange = NSMakeRange(index, 0);

        [self.inputDelegate selectionDidChange:self];
    }
}
```


With an instance of the [UITextChecker](https://developer.apple.com/documentation/uikit/uitextchecker) class, you can check the spelling of a document or offer suggestions for completing partially entered words. When spell-checking a document, a `UITextChecker` object searches a document at a specified offset. When it detects a misspelled word, it can also return an array of possible correct spellings, ranked in the order which they should be presented to the user (that is, the most likely replacement word comes first). You typically use a single instance of `UITextChecker` per document, although you can use a single instance to spell-check related pieces of text if you want to share ignored words and other state.

The method you use for checking a document for misspelled words is [rangeOfMisspelledWordInString:range:startingAt:wrap:language:](https://developer.apple.com/documentation/uikit/uitextchecker/1621029-rangeofmisspelledwordinstring); the method used for obtaining the list of possible replacement words is [guessesForWordRange:inString:language:](https://developer.apple.com/documentation/uikit/uitextchecker/1621037-guessesforwordrange). You call these methods in the given order. To check an entire document, you call the two methods in a loop, resetting the starting offset to the character following the corrected word at each cycle through the loop, as shown in Listing 9-17.

__Listing 9-17__  Spell-checking a document

```objc
- (IBAction)spellCheckDocument:(id)sender {
    NSInteger currentOffset = 0;
    NSRange currentRange = NSMakeRange(0, 0);
    NSString *theText = textView.text;
    NSRange stringRange = NSMakeRange(0, theText.length-1);
    NSArray *guesses;
    BOOL done = NO;

    NSString *theLanguage = [[UITextChecker availableLanguages] objectAtIndex:0];
    if (!theLanguage)
        theLanguage = @"en_US";

    while (!done) {
        currentRange = [textChecker rangeOfMisspelledWordInString:theText range:stringRange
            startingAt:currentOffset wrap:NO language:theLanguage];
        if (currentRange.location == NSNotFound) {
            done = YES;
            continue;
        }
        guesses = [textChecker guessesForWordRange:currentRange inString:theText
            language:theLanguage];
        NSLog(@"---------------------------------------------");
        NSLog(@"Word misspelled is %@", [theText substringWithRange:currentRange]);
        NSLog(@"Possible replacements are %@", guesses);
        NSLog(@" ");
        currentOffset = currentOffset + (currentRange.length-1);
    }
}
```

The `UITextChecker` class includes methods for telling the text checker to ignore or learn words. Instead of just logging the misspelled words and their possible replacements, as the method in Listing 9-17 does, you should display some user interface that allows users to select correct spellings, tell the text checker to ignore or learn a word, and proceed to the next word without making any changes. One possible approach for an iPad app would be to use a popover view that lists the guesses in a table view and includes buttons such as Replace, Learn, Ignore, and so on.

You may also use `UITextChecker` to obtain completions for partially entered words and display the completions in a table view in a popover view. For this task, you call the [completionsForPartialWordRange:inString:language:](https://developer.apple.com/documentation/uikit/uitextchecker/1621034-completions) method, passing in the range in the given string to check. This method returns an array of possible words that complete the partially entered word. Listing 9-18 shows how you might call this method and display a table view listing the completions in a popover view.

__Listing 9-18__  Presenting a list of word completions for the current partial string

```objc
- (IBAction)completeCurrentWord:(id)sender {

    self.completionRange = [self computeCompletionRange];
    // The UITextChecker object is cached in an instance variable
    NSArray *possibleCompletions = [textChecker completionsForPartialWordRange:self.completionRange
        inString:self.textStore language:@"en"];

    CGSize popOverSize = CGSizeMake(150.0, 400.0);
    completionList = [[CompletionListController alloc] initWithStyle:UITableViewStylePlain];
    completionList.resultsList = possibleCompletions;
    completionListPopover = [[UIPopoverController alloc] initWithContentViewController:completionList];
    completionListPopover.popoverContentSize = popOverSize;
    completionListPopover.delegate = self;
    // rectForPartialWordRange: is a custom method
    CGRect pRect = [self rectForPartialWordRange:self.completionRange];
    [completionListPopover presentPopoverFromRect:pRect inView:self
        permittedArrowDirections:UIPopoverArrowDirectionAny animated:YES];
}
```

[Next](Document%20Revision%20History.md)[Previous](Using%20Text%20Kit%20to%20Draw%20and%20Manage%20Text.md)

