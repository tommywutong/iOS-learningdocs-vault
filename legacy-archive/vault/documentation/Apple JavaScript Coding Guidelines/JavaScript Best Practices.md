---
title: Apple JavaScript Coding Guidelines
apple_id: TP40006088
resource_type: Guide
platform: Safari|macOS
topic: Languages & Utilities
technology: null
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/documentation/ScriptingAutomation/Conceptual/JSCodingGuide/Advanced/Advanced.html
archived_at: '2026-07-18T02:05:35.838720Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Apple JavaScript Coding Guidelines](Introduction%20to%20Apple%20JavaScript%20Coding%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Object-Oriented%20JavaScript.md)

# JavaScript Best Practices

There are a number of considerations that you should take into account when writing JavaScript code. Whether you’re trying to tune your code for better performance or test it for compatibility, these best practices can help your code perform better and be more compatible.

If you’re looking for performance and testing tips for JavaScript coding, read this chapter.

This section includes a number of tips for minimizing your JavaScript application’s memory footprint and helping it perform better.

- __Release initialization functions.__ Code that’s called once and never used again can be deleted after its execution. For instance, deleting a window’s `onload` handler function releases any memory associated with the function, like this:

```
var foo = function()
{
    // code that makes this function work
    delete foo;
}
window.addEventListener('load', foo, false);
```
- __Use delete statements.__ Whenever you create an object using a `new` statement, pair it with a `delete` statement. This ensures that all of the memory associated with the object, including its property name, is available for garbage collection. The `delete` statement is discussed more in [Freeing Objects](Object-Oriented%20JavaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmzzfvjvomi).
- __Test for an element’s existence.__ Before using nonstandard elements, check for their existence like this:

```
if ( "innerHTML" in document.getElementById("someDiv") )
{
    // code that works with innerHTML
}
```
- __Avoid evaluated statements.__ Using the `eval` function disables performance and memory optimizations in the JavaScript runtime. Consider using function variables, as discussed in [Functions](JavaScript%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dknbqfvjvomq), in cases where you are passing in lines of code to another function, like `setTimeout` or `setInterval`.

When creating a JavaScript application, consider these tips for testing your code.

- __Try multiple browsers.__ It’s a good practice to try any web-based JavaScript code you write in many browsers. In addition to the version of Safari included with Mac OS X, consider trying your code on these browsers:

  - WebKit nightly - [http://nightly.webkit.org/](http://nightly.webkit.org/)
  - Mozilla Firefox - [http://www.mozilla.com/firefox/](http://www.mozilla.com/firefox/)
  - Opera - [http://www.opera.com/](http://www.opera.com/)
- __Try other toolkit versions.__ If you’re using a third-party JavaScript toolkit such as Dojo, MochiKit, or prototype, try different versions of the library to see if your code uses the library properly.
- __Try a verifier.__ JavaScript verifiers such as [JSLint](http://www.jslint.com/) are useful at pinpointing compatibility problems and cases where the JavaScript code you wrote doesn’t conform to standards.

When writing JavaScript code, it’s good practice to avoid placing code and variables within the global scope of the file. Here are some considerations to consider regarding global scope:

- __Store data in the DOM tree, in cookies, or in HTML 5 client-side storage objects.__ The DOM tree, cookies, and HTML 5 client-side storage are good ways to conceal data to avoid conflicts with pages outside your domain. For performance reasons, you should generally limit use of these techniques to infrequently-used data, but any of these three techniques is better than using global variables.

  You can store data in the DOM tree like this:

```
/* Store data in the DOM tree */
var DOMobj = document.getElementById('page_globals');
DOMobj.setAttribute('foo', myIntegerVar);

/* for large text content, consider using this: */
DOMobj.style.display = "none";
DOMobj.innerHTML = myStringVar;

/* or this: */

DOMobj.style.display = "none";
if (typeof(DOMobj.innerText) != 'undefined') {
    // Internet Explorer workaround
    DOMobj.innerText = myStringVar;
} else {
    // Per the W3C standard
    DOMobj.textContent = myStringVar;
}

/* Recall the data later */
var DOMobj = document.getElementById('page_globals');
var myIntegerVar = parseInt(DOMobj.getAttribute('foo'));

/* Recall the large text data with this: */
var myStringVar = DOMobj.innerHTML;

/* or this: */

var myStringVar;
if (typeof(DOMobj.innerText) != 'undefined') {
    // Internet Explorer workaround
    myStringVar = DOMobj.innerText;
} else {
    // Per the W3C standard
    myStringVar = DOMobj.textContent;
}
```

  You can also store data in cookies using the `cookie` attribute of the `document` object. The syntax for creating and expiring cookies is somewhat complex and easy to get wrong. Thus, this method is discouraged as a global variable alternative unless you already have code for creating and modifying cookies. To learn more about cookies in JavaScript, read [http://www.quirksmode.org/js/cookies.html](http://www.quirksmode.org/js/cookies.html).

  Finally, for data that should persist across page loads, you can use HTML 5 client-side storage as described in _[Safari Client-Side Storage and Offline Applications Programming Guide](../iPhone/Safari%20Client-Side%20Storage%20and%20Offline%20Applications%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjw)_. Safari 3.1 and later provides both SQL database and local key-value storage.
- __Use the var keyword.__ Any variable created without the `var` keyword is created at the global scope and is not garbage collected when the function returns (because it doesn’t go out of scope), presenting the opportunity for a memory leak.
- __Use a global array, global object, or namespace prefix.__ If you need global variables, use a global object that contains all of the global variables, like this:

```
var myBulletinBoardAppGlobals = {
    foo: "some value",
    bar: null
};
```

  Or consider using a namespace prefix:

```
CPWFoo = "some value";
CPWBar = null;
```

  These practices prevent your global variables from colliding with global DOM objects present in the runtime.
- __Use an initialization function.__ If you have code that’s run immediately when the JavaScript is loaded, place it in a function that’s called when the window loads, like this:

```
myBulletinBoardAppGlobals.foo = function()
{
    // code that makes this function work
    delete myBulletinBoardAppGlobals.foo;
}
window.addEventListener('load', globals.foo, false);
```


JavaScript toolkits enhance productivity but often carry a significant memory footprint that may slow down your JavaScript application. When using a toolkit, try to reduce the toolkit’s footprint to just the APIs that you use in your application.

Also, if you’re developing a Dashboard widget, try to avoid bundling the Apple-provided Apple Classes within your widget; instead, follow the instructions provided in [Introduction to the Apple Classes](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AppleClasses.html#//apple_ref/doc/uid/TP40003186).

[Next](Document%20Revision%20History.md)[Previous](Object-Oriented%20JavaScript.md)

