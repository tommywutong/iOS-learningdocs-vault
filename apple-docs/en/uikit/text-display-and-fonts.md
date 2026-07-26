---
title: Text display and fonts
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/text-display-and-fonts
source_url: 'https://developer.apple.com/documentation/uikit/text-display-and-fonts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/text-display-and-fonts.json'
content_hash: 'sha256:b93150bfe672d6ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Text display and fonts

<sub>API Collection</sub>

Display text, manage fonts, and check spelling.

## Topics

### Text views

- [UILabel](uilabel.md) — A view that displays one or more lines of informational text.
- [UITextField](uitextfield.md) — An object that displays an editable text area in your interface.
- [UITextView](uitextview.md) — A scrollable, multiline text region.
- [Drag and drop customization](drag-and-drop-customization.md) — Extend the standard drag and drop support for text views to include custom types of content.

### Text bounds sizing

- [UILetterformAwareAdjusting](uiletterformawareadjusting.md) — The typographic bounds-sizing behavior to handle text with fonts that contain oversize characters.

### Text formatting

- [UITextFormattingCoordinator](uitextformattingcoordinator.md) — An object that coordinates text formatting using the standard Mac font panel.
- [UITextAttributesConversionHandler](uitextattributesconversionhandler.md) — A handler for updating text with current font panel settings.

### Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Adding a custom font to your app](adding-a-custom-font-to-your-app.md) — Add a custom font to your app and use it in your app’s interface.
- [UIFont](uifont.md) — An object that provides access to the font’s characteristics.
- [UIFontDescriptor](uifontdescriptor.md) — A collection of attributes that describes a font.
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [UIFontMetrics](uifontmetrics.md) — A utility object for obtaining custom fonts that scale to support Dynamic Type.

### Font picker

- [UIFontPickerViewController](uifontpickerviewcontroller.md) — A view controller that manages the interface for selecting a font that the system provides or the user installs.
- [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md) — A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) — The filters and display settings a font picker view controller uses to set up a font picker.

### Spell checking

- [UITextChecker](uitextchecker.md) — An object to check a string (usually the text of a document) for misspelled words.

### Text manipulations

- [init(_:)](<../coretext/cttextalignment/init(__).md>) — Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.
- [NSTextAlignmentFromCTTextAlignment](<nstextalignment/init(__).md>) — Converts a Core Text alignment constant value to the matching constant value in UIKit.

### Metrics

- [UITextPosition](uitextposition.md) — A position in a text container—that is, an index into the backing string in a text-display view.
- [UITextRange](uitextrange.md) — A range of characters in a text container with a starting index and an ending index in string backing a text-entry object.
- [UITextSelectionRect](uitextselectionrect.md) — An encapsulation of information about a selected range of text in a document.

## See Also

### Text

- [TextKit](textkit.md) — Manage text storage and perform custom layout of text-based content in your app’s views.
- [Keyboards and input](keyboards-and-input.md) — Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Writing Tools](writing-tools.md) — Add support for Writing Tools to your app’s text views.
- [Handwriting recognition](handwriting-recognition.md) — Configure text fields and custom views that accept text to handle input from Apple Pencil.
