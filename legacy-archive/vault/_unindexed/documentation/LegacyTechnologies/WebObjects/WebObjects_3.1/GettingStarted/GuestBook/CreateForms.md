---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/CreateForms.html
archived_at: '2026-07-15T07:48:40.493207Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](CreateInputFields.md)

## Create form-based dynamic HTML elements

You need to add dynamic HTML elements to capture the guest's input. You'll do this by creating a form.

- Place the cursor on the line after the "My Guest Book" text and press Enter.
- Click the palette button on the main window to open the palette window.

The palette window contains three different palettes from which you can choose ready-built elements. The first contains static HTML elements, the second contains form-based dynamic HTML elements, and the third contains abstract dynamic elements (objects that have no true HTML equivalent).

- In the palette window, click the middle icon to display the Form Elements palette.
- Drag a form object from the palette onto the page.

A pre-defined form with two text fields and Submit and Reset buttons appears. This form is just a template that you can modify.

!- Select the word "Field" in front of the first text field and type __Name__ in its place.
- Select the word "Field" in front of the second text field and type __E-mail__ in its place.
- Place the cursor below the text fields, and drag a multi-line text element onto the page.
- Click the multi-line text element once to select it, and then resize it.
!- Choose File!Save to save the Main component.

### A closer look

You just created what look like the form elements defined in the HTML specification. However, what you've really created are several WebObjects dynamic elements: a WOForm, two WOTextFields, a WOText, a WOSubmitButton, and a WOResetButton. These dynamic elements look and act like HTML form elements but have the same programming interface as other WebObjects elements.
Notice that before you dragged the form or the multi-line text element from the palette, you had to set the cursor position. Because an HTML file is a text flow, you can't just drag an element to any point on the window. You must place the cursor where you want the element, using hard returns if necessary, and then add the element. If you have text selected when you drag, the element will replace the selection.

[!Table of Contents](GuestBook.book.md) [!Next Section](CreateVariables.md)
