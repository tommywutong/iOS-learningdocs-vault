---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/JavaScript_js_cloudkit_code_samples_authentication_js.html
archived_at: '2026-07-18T03:03:25.173667Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](JavaScript-js-cloudkit-code-samples-public-query.js.md)[Previous](JavaScript-js-cloudkit-code-samples-private-subscriptions.js.md)

# JavaScript/js/cloudkit-code-samples/authentication.js

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The authentication sample code with some helper functions to render the username/user record name and to construct
    the auth button containers.
*/
CKCatalog.tabs['authentication'] = (function() {

  var displayUserName = function(name) {
    var userNameEl = document.getElementById('username');
    userNameEl.textContent = name;
    var displayedUserName = document.getElementById('displayed-username');
    if(displayedUserName) {
      displayedUserName.textContent = name;
    }
  };

  var createButtonContainersHTML = function() {
    return '<div>'+
      '<h2 id="displayed-username"></h2>'+
      '<div id="apple-sign-in-button"></div>'+
      '<div id="apple-sign-out-button"></div>'+
    '</div>';
  };

  var showDialogForPersistError = function() {
    var html = '<h2>Unable to set a cookie</h2><p>';

    if(window.location.protocol === 'file:') {
      html += 'The authentication option <code>persist = true</code> is not compatible with the <i>file://</i> protocol. ';
    }

    html += 'Please edit <i>js/init.js</i> and set <code>persist = false</code> in <i>CloudKit.configure()</i>.</p>';

    CKCatalog.dialog.show(html, { title: 'Close' });
  };

  var authSample = {
    run: function() {
      var content = this.content;
      content.innerHTML = createButtonContainersHTML();
      return this.sampleCode().then(function() {
        return content.firstChild;
      });
    },
    sampleCode: function demoSetUpAuth() {

      // Get the container.
      var container = CloudKit.getDefaultContainer();

      function gotoAuthenticatedState(userInfo) {
        if(userInfo.isDiscoverable) {
          displayUserName(userInfo.firstName + ' ' + userInfo.lastName);
        } else {
          displayUserName('User record name: ' + userInfo.userRecordName);
        }
        container
          .whenUserSignsOut()
          .then(gotoUnauthenticatedState);
      }
      function gotoUnauthenticatedState(error) {

        if(error && error.ckErrorCode === 'AUTH_PERSIST_ERROR') {
          showDialogForPersistError();
        }

        displayUserName('Unauthenticated User');
        container
          .whenUserSignsIn()
          .then(gotoAuthenticatedState)
          .catch(gotoUnauthenticatedState);
      }

      // Check a user is signed in and render the appropriate button.
      return container.setUpAuth()
        .then(function(userInfo) {

          // Either a sign-in or a sign-out button was added to the DOM.

          // userInfo is the signed-in user or null.
          if(userInfo) {
            gotoAuthenticatedState(userInfo);
          } else {
            gotoUnauthenticatedState();
          }
        });
    }
  };

  return [ authSample ];

})();
```

[Next](JavaScript-js-cloudkit-code-samples-public-query.js.md)[Previous](JavaScript-js-cloudkit-code-samples-private-subscriptions.js.md)

