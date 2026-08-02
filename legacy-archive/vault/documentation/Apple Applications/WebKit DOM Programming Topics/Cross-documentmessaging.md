---
title: WebKit DOM Programming Topics
apple_id: TP40001483
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: WebKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/Cross-documentmessaging.html
archived_at: '2026-07-15T05:18:09.337837Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit DOM Programming Topics](index.md)



## Cross-Document Messaging

As a general rule, scripts loaded by web content served from one origin (host and domain) cannot access web content served by a different origin. This is an important security feature that prevents a multitude of different security attack vectors. However, it also makes it difficult for scripts to interact with one another across these boundaries.

To make communication between documents from different origins easier, the HTML 5 specification adds cross-document messaging. This feature is supported in Safari 4.0 and later.

### Posting a Message to a Window

To post a message, you must first obtain the `Window` object of the document you want to message. In effect, this means that you can post messages only to:

- other frames or inline frames within your document window (or their descendants if all intermediate frames or inline frames were served from the same origin).

  1. `var iFrameObj = document.getElementById('myId');`
  2. `var windowObj = iFrameObj.contentWindow;`
- windows that your document explicitly opened through JavaScript calls.

  1. `var windowObj = window.open(...);`
- the window that contains your document window, the window that contains that window, and so on up to the root window.

  1. `var windowObj = window.parent;`
- the window that opened your document.

  1. `var windowObj = window.opener;`

Once you have obtained the `Window` object for the target document, you can send it a message with the following code:

1. `windowObj.postMessage('test message', 'http://example.com');`

The first parameter is an arbitrary message.

The second parameter is the target origin value. An origin value is just a URL with the path part removed. For example, the origin of a local file is `file://`. By specifying a target origin, you are saying that that your message should only be delivered if the target window’s current contents came from that origin.

Although you may specify an asterisk (`*`) wildcard for the target origin (to allow the message to be sent regardless of where the contents of the target window came from), you should do so only if you are certain that it would not be harmful if your message were received by content originating from a different website.

### Receiving a Message Posted to a Window

To receive messages, you must add an event listener for the `message` event type to your document’s `window` object. To do this, use the following code:

1. `function messageReceive(evt) {`
2. `if (evt.origin == 'http://example.com') {`
3. `// The message came from an origin that`
4. `// your code trusts. Work with the message.`
5. `alert('Received data '+evt.data);`
7. `// Send a message back to the source:`
8. `evt.source.postMessage('response', evt.origin);`
9. `} else {`
10. `alert('unexpected message from origin '+evt.origin);`
11. `}`
12. `}`
13. `window.addEventListener('message', messageReceive, false);`

The `message` event you receive has three properties of interest:

- `data`—the message contents.
- `origin`—the domain from which the message was sent (`http://example.com` in this case).
- `source`—the window from which the message was sent.

### A Service Discovery Example: Message Boxes

This section contains two code listings: `index.html` and `msg_contents.html` that, when combined, implement basic service discovery and data relaying on top of the cross-document messaging architecture.

To use this code, you must first do the following things:

- Install Safari 4.0 or later, or install a recent WebKit nightly.
- Save the contents of the two code listings in separate files.
- In the file `msg_contents.html`, modify the variable `allowed_origins` to contain a list of origins from which you plan to serve the `index.html` or `msg_contents.html` file.

  For example, if you intend to place this file at `http://www.example.org/message_test/msg_contents.html`, you should make sure that `'http://www.example.org'` (enclosed in quotes) is a key in the `allowed_origins` object.

  If you only have one machine, turn on web sharing, then use `http://localhost` as one origin and `file://` as the other.
- In the file `msg_contents.html`, optionally change the variable `root_origin` to the actual expected origin of the top level HTML page.
- Place a copy of the modified `msg_contents.html` file on the desired server or servers.
- In the file `index.html`, replace the `allowed_origins` declaration with the one from your `msg_contents.html` file. Then, update the `boxes` object to provide the URLs for the `msg_contents.html` files you just put on your servers.

  If you only have one machine, use a `file://` URL pointing to the path of the `msg_contents.html` file. For example, if you placed the file in `/Library/WebServer/Documents/message_test/msg_contents.html`, the local URL would be `file:///Library/WebServer/Documents/message_test/msg_contents.html`.
- Place this modified `index.html` file on one of the servers and navigate to the URL, or open it as a local file on disk.

Once you have completed these steps, you should see several boxes, one per entry in the `boxes` object. Each of these boxes should contain a small form with a text input box, a series of checkboxes (one for each of the outer boxes), and a submit button.

If you type something into the text box, check one of the checkboxes, and click submit, the text should appear at the bottom of the window whose name corresponds with the checkbox.

__Listing 8-1__Cross-document messaging example: index.html

1. `<html><head>`
2. `<script language='javascript' type='text/javascript'><!--`
3. `/*global alert, navigator, document, window */`

6. `var window_list = [];`
7. `var origin_list = [];`
9. `var boxes = {`
10. `local: "http://host1.domain1.top/messages2/msg_contents.html",`
11. `remote: "http://host2.domain2.top/messages2/msg_contents.html",`
12. `third: "http://host3.domain3.top/messages2/msg_contents.html"`
13. `};`
15. `var allowed_origins = {`
16. `'http://host1.domain1.top': 1,`
17. `'http://host2.domain2.top': 1,`
18. `'http://host3.domain3.top': 1`
19. `};`
21. `function smartsplit(string, pattern, count)`
22. `{`
23. `// alert('string '+string);`
24. `// alert('pattern "'+pattern+'"');`
25. `// alert('count '+count);`
27. `var lastpos = count - 1;`
29. `var arr = string.split(/ /);`
30. `// alert('AC: '+arr.length+" "+string);`
31. `if (arr.length > lastpos) {`
32. `var temparr = [];`
33. `for (var i=lastpos; i<arr.length; i++) {`
34. `temparr[i-lastpos] = arr[i];`
35. `arr[i] = undefined;`
36. `}`
37. `arr[lastpos] = temparr.join(pattern);`
38. `}`
39. `return arr;`
40. `}`
42. `function listWindows()`
43. `{`
44. `var retstring = "";`
45. `for (var i in origin_list) {`
46. `if (origin_list.hasOwnProperty(i)) {`
47. `// alert('UUID: '+i+' Origin: '+origin_list[i]);`
48. `retstring += i+' '+origin_list[i]+'\n';`
49. `}`
50. `}`
51. `return retstring;`
52. `}`

55. `function messageReceive(evt) {`
56. `var windowlist;`
58. `if (evt.origin === null || evt.origin in allowed_origins) {`
59. `var arr = smartsplit(evt.data, " ", 2);`
61. `if (arr[0] == 'sendto') {`
62. `// usage: sendto UUID remote_origin message`
63. `arr = smartsplit(evt.data, " ", 4);`
64. `var remote_window = window_list[arr[1]];`
65. `remote_window.postMessage('sendto_output '+arr[3], arr[2]);`
66. `} else if (arr[0] == 'register') {`
67. `// usage register UUID`
68. `var name = arr[1];`
70. `if (window_list[name]) {`
71. `// name conflict.`
72. `var add=1;`
73. `while (window_list[name+'_'+add]) {`
74. `add++;`
75. `}`
76. `name = name+'_'+add;`
77. `evt.source.postMessage("register_newid "+name, evt.origin);`
78. `}`
80. `window_list[name] = evt.source;`
81. `origin_list[name] = evt.origin;`
82. `windowlist = listWindows();`
83. `for (var windowid in window_list) {`
84. `if (window_list.hasOwnProperty(windowid)) {`
85. `// alert('windowid: '+windowid);`
86. `window_list[windowid].postMessage("list_output "+windowlist, origin_list[windowid]);`
87. `}`
88. `}`
89. `} else if (arr[0] == 'list') {`
90. `// usage list`
91. `windowlist = listWindows();`
92. `evt.source.postMessage("list_output "+windowlist, evt.origin);`
93. `} else {`
94. `alert('unknown command '+arr[0]);`
95. `}`
96. `} else {`
97. `alert('unexpected message from origin '+evt.origin);`
98. `}`
99. `}`
101. `function dosetup()`
102. `{`
103. `if (navigator.userAgent.match(/Safari/)) {`
104. `var version = parseFloat(navigator.userAgent.replace(/.*AppleWebKit\//, "").replace(/[^0-9.].*$/, ""));`
106. `if (version < 528) {`
107. `alert('WebKit version '+version+' does not support this application.');`
108. `}`
110. `}`
111. `// for (var i=0; i<nchannels; i++) {`
112. `// alert('setup channel '+i);`
113. `// channel[i] = new MessageChannel();`
114. `// }`
115. `window.addEventListener('message', messageReceive, false);`
117. `var boxstr = "";`
118. `for (var i in boxes) {`
119. `if (boxes.hasOwnProperty(i)) {`
120. `boxstr += "<iframe height='600' id='"+i+"' src='"+boxes[i]+"'></iframe>\n";`
121. `}`
122. `}`
123. `var boxlistdiv = document.getElementById('boxlist');`
124. `boxlistdiv.innerHTML = boxstr;`
125. `}`
127. `dosetup();`
129. `--></script>`
130. `</head>`
131. `<body onload='dosetup();'>`
132. `<div id='boxlist'>`
133. `</div>`
134. `</body>`
135. `</html>`

__Listing 8-2__Cross-document messaging example: msg_contents.html

1. `<html><head>`
2. `<script language='javascript' type='text/javascript'><!--`
3. `/*global alert, document, window, navigator */`
5. `var allowed_origins = {`
6. `'http://stavromula-beta.apple.com': 1,`
7. `'http://holst.apple.com': 1`
8. `};`
10. `var received_root_origin = '';`
12. `var root_origin = '*';`
14. `function smartsplit(string, pattern, count)`
15. `{`
16. `// alert('string '+string);`
17. `// alert('pattern "'+pattern+'"');`
18. `// alert('count '+count);`
20. `var lastpos = count - 1;`
22. `var arr = string.split(/ /);`
23. `// alert('AC: '+arr.length+" "+string);`
24. `if (arr.length > lastpos) {`
25. `var temparr = [];`
26. `for (var i=lastpos; i<arr.length; i++) {`
27. `temparr[i-lastpos] = arr[i];`
28. `arr[i] = undefined;`
29. `}`
30. `arr[lastpos] = temparr.join(pattern); }`
31. `return arr;`
32. `}`
34. `function mkcheckbox(inpstr)`
35. `{`
36. `var str = "";`
38. `var arr = inpstr.split("\n");`
39. `for (var entid in arr) {`
40. `if (arr.hasOwnProperty(entid)) {`
41. `var ent = arr[entid];`
42. `if (ent !== "") {`
43. `// alert('ent: '+ent);`
44. `var bits = smartsplit(ent, " ", 2);`
45. `str += "<input type=checkbox name='"+ent+"'>"+bits[0]+"</input>\n";`
46. `}`
47. `}`
48. `}`
49. `return str;`
50. `}`
52. `function messageReceive(evt) {`
53. `if (evt.origin === null || evt.origin in allowed_origins) {`
55. `// The message came from an origin that`
56. `// your code trusts. Work with the message.`
58. `// alert('Received data: '+evt.data);`
59. `// var tmp = 'Test this, please';`
60. `// var x = smartsplit(tmp, " ", 2);`
61. `// alert('x[0] = '+x[0]);`
62. `// alert('x[1] = '+x[1]);`
63. `// alert('x[2] = '+x[2]);`
65. `var arr = smartsplit(evt.data, " ", 2);`
66. `if (arr[0] == 'list_output') {`
67. `if (evt.origin == root_origin || root_origin == '*') {`
68. `var div2 = document.getElementById('temp2');`
69. `div2.innerHTML = mkcheckbox(arr[1]);`
70. `received_root_origin = evt.origin;`
71. `// alert('arr[1] = '+arr[1]);`
72. `} else {`
73. `alert('received list_output message from unexpected origin: '+evt.origin);`
74. `}`
75. `} else if (arr[0] == 'sendto_output') {`
76. `// alert('Received data: '+evt.data);`
77. `var div3 = document.getElementById('temp3');`
78. `div3.innerHTML += arr[1]+'<br />\n';`
79. `} else if (arr[0] == 'register_newid') {`
80. `var mydiv = document.getElementById('temp');`
81. `mydiv.innerHTML = arr[1]+" box";`
82. `}`
84. `// Send a message back to the source:`
85. `// evt.source.postMessage('response', evt.origin);`
86. `} else {`
87. `alert('unexpected message from origin '+evt.origin);`
88. `}`
89. `}`
91. `function setup_listener()`
92. `{`
93. `window.addEventListener('message', messageReceive, false);`
94. `}`
96. `function setup()`
97. `{`
98. `var mydiv = document.getElementById('temp');`
100. `// mydiv.innerHTML = 'Test';`
101. `// mydiv.innerHTML = ' '+bigdoc;`
103. `// If we can access the document object, we are locally loaded and should`
104. `// talk to the remotely-loaded window. Otherwise, the reverse`
105. `// is true.`
107. `var myid = '';`
108. `if (window.parent.document) {`
109. `myid = 'local';`
110. `} else {`
111. `myid = 'remote';`
112. `}`
114. `mydiv.innerHTML = myid+" box";`
115. `// window.addEventListener('message', messageReceive, false);`
116. `setup_listener();`
118. `var topwindow = window;`
119. `while (topwindow.parent && (topwindow.parent != topwindow)) { topwindow = topwindow.parent; }`
121. `topwindow.postMessage('register '+myid, root_origin);`
122. `// window.parent.postMessage('list', '*');`
124. `}`
126. `function sendmsg()`
127. `{`
128. `var message = document.getElementById('sendtext').value;`
129. `var mydiv2 = document.getElementById('temp2');`
130. `var checkboxes = mydiv2.children;`
132. `// alert('checkboxes: '+checkboxes);`
133. `var topwindow = window;`
134. `while (topwindow.parent && (topwindow.parent != topwindow)) { topwindow = topwindow.parent; }`
136. `for (var boxid in checkboxes) {`
137. `if (checkboxes.hasOwnProperty(boxid)) {`
138. `var checkbox = checkboxes[boxid];`
140. `// alert('checkbox: '+checkbox);`
141. `if (checkbox.tagName == "INPUT") {`
142. `// alert('input');`
143. `if (checkbox.checked) {`
144. `// alert('checked');`
145. `var arr = smartsplit(checkbox.name, " ", 2);`
146. `var uuid = arr[0];`
147. `var origin = arr[1];`
148. `// alert('send to: '+uuid+' origin '+origin);`
150. `// alert('topwindow is '+topwindow);`
151. `topwindow.postMessage('sendto '+uuid+' '+origin+' '+message, received_root_origin);`
152. `}`
153. `}`
154. `}`
155. `}`

158. `return false;`
159. `}`

162. `--></script>`
163. `</head><body onload='setup();'>`
164. `<div id='temp'></div>`
165. `<form onsubmit='return false;'>`
166. `<input type='text' id='sendtext'></input>`
167. `<input type='submit' value='submit' onclick='sendmsg();'></input>`
168. `<div id='temp2'></div>`
169. `</form>`
170. `<div id='temp3'></div>`
172. `</body></html>`

You can create numerous interesting extensions on top of this sort of design. For example, you might add a command message that asks the window at the other end what commands it supports, then communicate with it if you share a common set of commands. The possibilities are limitless.

### Security Considerations

There are several key things you should be aware of when using cross-document messaging:

- Obtaining `Window` objects for other windows is not always easy. Scripts running in a window, frame, or `iframe` element served from one origin cannot access the DOM tree of documents served from a different origin, and thus cannot get access to the `Window` objects of other `iframe` elements within such a window.

  Among other things, this means that two `iframe` elements from different domains cannot directly obtain each other’s `Window` objects because one or the other is (by definition) from a different origin than the document containing the `iframe` elements. In this situation, there are two possible solutions.

  The easiest solution is to have both windows discover each other using the parent window as a communications hub. This solution is also the most general solution because it works even if neither window can see the element containing the other window.

  Alternatively, the window with access to the parent window’s DOM tree could discover the other one and initiate communication. By doing so, the second window receives the first window’s `Window` object by way of the `source` field in the event object.

  > [!NOTE]
  > 
- Sending data to other windows can be dangerous, particularly if that information contains login information or other sensitive data. You should almost always take advantage of the target origin field when sending messages to avoid interception by content served by other sites. You should only use the wildcard asterisk (`*`) target origin value if you are absolutely sure that the data is harmless.
- Receiving data from other windows can also be dangerous. You should generally check the origin field when receiving messages to make sure that the data was sent from a website that you trust to some degree.

  Where possible, you should also check any received data for validity before using it. In particular, you should generally avoid executing JavaScript code received from another window (with the possible exception of JSON objects after careful validity checking).

As with any software, for maximum reliability and security, you should write your output code carefully to minimize the risk of causing problems for other code, and you should write your code under the assumption that other code is maliciously trying to attack your code, and thus you should perform type, bounds, and other sanity checks accordingly.

[Sending Notifications](SendingNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmzsfvjvomi)

[Calling Objective-C Methods](ObjCFromJavaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiytklkcijbuerskinca)
