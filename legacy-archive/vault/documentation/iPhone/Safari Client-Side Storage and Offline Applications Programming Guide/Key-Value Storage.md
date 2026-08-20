---
title: Safari Client-Side Storage and Offline Applications Programming Guide
apple_id: TP40007256
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Data Management
technology: null
published: '2011-09-21'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SafariJSDatabaseGuide/Name-ValueStorage/Name-ValueStorage.html
archived_at: '2026-07-18T02:27:25.761556Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Client-Side Storage and Offline Applications Programming Guide](Introduction.md)


[Next](Relational%20Database%20Basics.md)[Previous](HTML5%20Offline%20Application%20Cache.md)

# Key-Value Storage

Key-value storage allows you to store data locally, in either a session store or a local store. The `localStorage` and `sessionStorage` JavaScript objects are functionally identical except in their persistence and scope rules:

- The `localStorage` object is used for long-term storage. Data persists after the window is closed and is shared across all browser windows.
- The `sessionStorage` object is used for ephemeral data related to a single browser window. Data stored in the `sessionStorage` object does not persist after the window is closed and is not shared with other windows.

Key-value storage is similar to cookie storage; the storage objects are specific to a domain. Because key-value data is not sent back to the server along with every HTTP request, however, it is possible to store larger quantities of data with key-value storage than is practical with cookies. (If you need to send the stored data back to the server, you can do so explicitly using JavaScript and an `XMLHttpRequest` object.)

The examples in this section use local storage. You can change these examples to use session storage by substituting `sessionStorage` for `localStorage` wherever `localStorage` appears in the code.

The easiest way to store key-value data is to synthesize a property of the `sessionStorage` or `localStorage` object by setting the property to a value. For example:

`localStorage.shirt_size="Medium";`

In the example just given, if the property `localStorage.shirt_size` does not yet exist, it is created. If the property already exists, its value is reset.

You can also store a value in key-value storage using the `setItem()` method. This method takes two parameters: a key name and a value. For example:

```
// Store the value of the variable "myShirtSize" as the
// value of the field named "shirt_size".
localStorage.setItem("shirt_size", myShirtSize);
```

Storing data can throw an exception if you exceed a browser-specific quota. If the data you are storing is important, you should check for this exception and handle it. For example:

```
try {
    sessionStorage.setItem("shirt_size", myShirtSize);
} catch (e) {
    if (e == QUOTA_EXCEEDED_ERR) {
        alert('Unable to save preferred shirt size.');
    }
}
```

If your key name is a valid JavaScript token (no spaces, punctuation other than underscore, and so on) you can retrieve a value from key-value storage using the key as a property of the `localStorage` or `sessionStorage` object. For example:

`myShirtSize = localStorage.shirt_size`

Alternatively, you can use the `getItem()` method to retrieve data, passing in the key:

```
var myShirtSize = localStorage.getItem("shirt_size");
```

If no key-value pair with the specified key exists, `localStorage` returns `null` as the value.

You can find the total number of items in storage for your domain by examining the storage object’s `length` property. For example:

```
alert('there are ' + localStorage.length + ' items in the storage array.');
```

You can obtain a list of existing keys using the storage object’s `key()` method (again, using the `length` property to determine the number of keys).

```
var keyNames[];
var values[];
// iterate through array
var numKeys = localStorage.length;
for(i=0;i<numKeys;i++) {
    // get key name into an array
    keyNames[i]=localStorage.key(i);
    // use key name to retreive value and store in array
    values[i]=localStorage.getItem(keyNames[i]);
}
```


There are two ways to delete values from key-value storage: individually or en masse. To delete a single value, call the `removeItem()` method, passing in the key:

```
localStorage.removeItem("shirt_size");
```

To remove all key-value pairs for your domain, call the `clear()` method:

```
sessionStorage.clear();
```


Like cookies, storage objects are a shared resource common to web content served from the same domain. All pages from the same domain share the same local storage object. Frames and inline frames whose contents are from the same origin also share the same session storage object because they descend from the same window.

Because the storage resource is shared, scripts running in multiple page contexts can potentially modify the data stored in a storage object that is actively being scrutinized or modified by a script running on a different page. If your scripts do not notice these changes, you may not get the results you expect.

To this end, storage objects generate an event of type `"storage"` whenever a script adds, deletes, or modifies a value in key-value storage. The event has a `key` property, a `newValue` property, and an `oldValue` property. If `newValue` is `null`, the key-value pair has been removed. If `oldValue` is `null`, a new key-value pair has been added.

To handle storage events, register your handler function as an event listener:

```
window.addEventListener('storage', myStorage_handler, false);
```

Once you have registered an event handler, the specified function (in this case, `myStorage_handler`) is called whenever a script modifies either local or session storage. Here is a simple handler that shows an alert for each field in a `storage` event:

```
function myStorage_handler(evt)
{
    alert('The modified key was '+evt.key);
    alert('The original value was '+evt.oldValue);
    alert('The new value is '+evt.newValue);
    alert('The URL of the page that made the change was '+evt.url);
    alert('The window where the change was made was '+evt.source);
}
```

This example, while simple, shows the five event fields relevant to a storage event. The fields are as follows:

**`key`**
: The key that was modified. If the session or local storage object is wiped with the `clear` method, the value of `key` is `null`.

**`oldValue`**
: The previous value of the modified key. If the key is newly created, the value of `oldValue` is `null`. If the storage object is wiped with the `clear` method, the value is also `null`.

**`newValue`**
: The current (new) value of the modified key. If the key is deleted with the `clear` method, the value of `key` is `null`. If the storage object is wiped with the `clear` method, the value is also `null`.

**`url`**
: The URL of the page that added, modified, or deleted the key. The `url` field is only available if the page that made the change is in the same browsing context (a single tab in a single window). Otherwise, the `url` field value will be `null`.

**`source`**
: The `Window` object containing the script that modified the key. The `source` field is only available if the page that made the change is in the same browsing context (a single tab in a single window). Otherwise, the `source` field value will be `null`.

The HTML page in Listing 2-1 demonstrates local key-value storage. If you modify the values in either field, they are stored locally (both on modification and on page exit). The values are retrieved from storage when you reload the page.

__Listing 2-1__  Key-value storage example

```
<html>
<head>
    <title>Key-Value Storage</title>
<script type="text/javascript">
var sizeMenu
var colorMenu

function init() {
    sizeMenu = document.getElementById("sizeMenu");
    colorMenu = document.getElementById("colorMenu");
    if (localStorage.shirtSize)
        sizeMenu.value = localStorage.shirtSize;
    if (localStorage.shirtColor)
        colorMenu.value = localStorage.shirtColor;
}

function saveChoice() {
    localStorage.shirtSize=sizeMenu.value;
    localStorage.shirtColor=colorMenu.value;
    console.log(localStorage.shirtSize + ", " + localStorage.shirtColor);
}
</script>
</head>

<body onload="init()">
<h2>Local Storage</h2>

<p> Shirt size:
<select id="sizeMenu" onchange="saveChoice()">
    <option value="small">Small</option>
    <option value="medium">Medium</option>
    <option value="large">Large</option>
</select>
</p>

<p> Shirt color:
<select id="colorMenu" onchange="saveChoice()">
    <option value="red">Red</option>
    <option value="white">White</option>
    <option value="blue">Blue</option>
    <option value="tiedye">Tie-Dyed</option>
</select>
</p>
</body>
</html>
```


You can inspect and debug key-value storage using the Web Inspector, as described in [Debugging Offline Applications](HTML5%20Offline%20Application%20Cache.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnznknlto). The display of stored data is not updated dynamically as the store changes; to refresh the display, click the “recycle” button in the bottom bar.

The Web Inspector shows the storage objects that exist for each domain that has created a local store. Local files share the same domain, so when debugging a website locally you may want to clear the local store during initialization; otherwise the local storage object may contain data created while testing files from another site locally. When inspecting local files, you may see data in local storage used by the Web Inspector itself.

In addition to inspecting the key-value store, you can interactively modify the storage contents using the Web Inspector. You can also use the Web Inspector to interactively debug JavaScript. For details, see _[Safari Web Inspector Guide](../../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

[Next](Relational%20Database%20Basics.md)[Previous](HTML5%20Offline%20Application%20Cache.md)

