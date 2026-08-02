---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AccessingResourcesWithinYourExtensionFolder/AccessingResourcesWithinYourExtensionFolder.html
archived_at: '2026-07-27T06:57:07.592394Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Adding%20Extension%20Bars.md)[Previous](Using%20Extension%20Builder.md)

# Accessing Resources Within Your Extension Folder

Your global HTML page, extension bars, injected scripts, and style sheets can all access resources within your extension folder, such as `.js` files, images, and other media. The resources must reside within your `.safariextension` folder when Extension Builder builds the extension (creates the compressed `.safariextz` package).

## Using Relative URLs

Relative URLs are resolved differently for injected scripts and other extension resources.

Used from an injected script, relative URLs are relative to the webpage the script is injected into. From within an injected script—or any of its subresources, such as included scripts—resources in the extension folder can be loaded only by using an absolute URL (see [Using Absolute URLs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjyfvjvomi)).

For all other extension resources, including injected style sheets, relative URLs are relative to the source file within the extension folder.

This means you can access resources within the extension folder using relative URLs from the global page, extension bars, injected style sheets, or any of their subresources.

You can have nested folders within your extension folder. For example, your extension folder could contain a Scripts folder and an Images folder.

```
MyExtension.safariextz/
   Scripts/
      myScript.js
   Images/
      myImage.png
```

You can traverse the folder hierarchy with a relative URL by using `../` to go up a level. For example, from a script in the Scripts folder, you could load an image in the Images folder using this snippet:

`img.src='../Images/myImage.png'`.

__Important:__ Do not begin a relative URL with a leading forward slash (`/`). Relative URLs must be relative to the file they are loaded from, not relative to the extension’s folder.

## Using Absolute URLs

You can use absolute URLs to access resources in your extension folder from any part of your extension.

Use of the `file:///` scheme is not allowed. Absolute URLs begin with `safari.extension.baseURI`, followed by the path within the folder and the filename. For example, using an absolute URL from a JavaScript function looks like this:

`img.src = safari.extension.baseURI + 'Images/myImage.png'`

__Important:__ The base URI ends in a forward slash. Do not begin the path with another.

You must use JavaScript to obtain the absolute URL, as it changes each time Safari is launched. To load a resource from an HTML or CSS file using an absolute URL, you need to add some JavaScript to the source file.

## Example: Loading a Background Image in CSS

An injected style sheet can add a background image to a website using images stored inside the extension. The easiest way to do this is to use a relative URL directly in CSS. For example:

`body { background-image:url('../Images/paper.jpg'); }`

To accomplish the same thing using an absolute URL, insert a few lines of JavaScript into your style sheet:

```
<script type = "text/javascript">
var myImage = safari.extension.baseURI + "Images/paper.jpg" ;
document.body.style.cssText = "background-image: url(" + myImage + ")";
</script>
```

## Security

Use of the `file:///` scheme is not allowed.

The base URI returns a unique value each time Safari is run. It must be obtained at least once per session by your extension. It does not persist from session to session and it is not predictable.

This prevents outside scripts from determining the base URI of your extension and accessing its resources.

You can capture the base URI for your extension in a string and reuse the string within your code during a session, but you cannot store the string and reuse it from session to session.

[Next](Adding%20Extension%20Bars.md)[Previous](Using%20Extension%20Builder.md)
