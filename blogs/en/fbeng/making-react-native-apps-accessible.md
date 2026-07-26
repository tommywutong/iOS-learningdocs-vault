---
title: Making React Native apps accessible
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/11/23/android/making-react-native-apps-accessible/'
original_language: en
published: 2015-11-23
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dc11df880404dba1'
translated: false
---

> 原文：[Making React Native apps accessible](https://engineering.fb.com/2015/11/23/android/making-react-native-apps-accessible/)　·　Meta Engineering — iOS

With the recent launch of React on web and React Native on mobile, we’ve provided a new front-end framework for developers to build products. One key aspect of building a robust product is ensuring that anyone can use it, including people who have vision loss or other disabilities. The Accessibility API for React and React Native enables you to make any React-powered experience usable by someone who may use assistive technology, like a screen reader for the blind and visually impaired.

For this post, we’re going to focus on React Native apps. We’ve designed the React Accessibility API to look and feel similar to the iOS and Android APIs. If you’ve developed accessible applications for the web, iOS, or Android before, you should feel comfortable with the framework and nomenclature of the React AX API. For instance, you can make a UI element _accessible_ (therefore exposed to assistive technology) and use _accessibilityLabel_ to provide a string description for the element:

`<View accessible={true} accessibilityLabel=”This is simple view”>`

Let’s walk through a slightly more involved application of the React AX API by looking at one of Facebook’s own React-powered products: the **Ads Manager app**.

The [Ads Manager app](https://www.facebook.com/business/news/ads-manager-app) allows advertisers on Facebook to manage their accounts and create new ads on the go. It’s Facebook’s first cross-platform app, and it was built with React Native.

Ads can be complicated, as there can be a lot of contextual information in them. When we were designing these interactions for accessibility, we decided to group related information together. For example, a campaign list item displays the campaigner’s name, campaign result, and campaign status in one single list item (e.g., “Hacker and Looper, Page Post Engagement, 29,967 Post Engagements, Status Active”).

![](https://engineering.fb.com/wp-content/uploads/2015/11/GPv5twD09sbsM4YBAHOGB2cAAAAAbj0JAAAB.jpg)

We can implement this behavior with React Native’s Accessibility API easily. We just need to set accessible={true} on the parent component, and it will then gather all accessibility labels from its children.

```javascript
<View
  accessible={true}
  style={{
    flex: 1,
    backgroundColor: 'white',
    padding: 10,
    paddingTop: 30,
  }}>
  <Text>Hacker and Looper, Page Post Engagement</Text>
  <Text>29,967 Post Engagements</Text>
  <AdsManagerStatus
    accessibilityLabel={'Status ' + this.props.status}
    status={this.props.status}
  />
</View>
```

Nested UI elements, such as a switch inside a table row, also require specific accessibility support. When a user highlights a row with a screen reader, we want all the information in that row to be read back, as well as to indicate that there is an actionable element inside that row. The Accessibility API provides the ability to fetch the accessibility environment from the system and to listen to setting changes from the system. Now we can simply change the parent’s behavior and inform the user through screen readers like VoiceOver or TalkBack (e.g., “double tap on row to toggle switch inside that row”). In the Ads Manager app, we use this switch to toggle the notification setting. When the row is highlighted, it will read out: “Ad Approved. On. Double tap to toggle setting.”

![](https://engineering.fb.com/wp-content/uploads/2015/11/GEP6twDwvtKrREYDAHKTGxUAAAAAbj0JAAAB.jpg)

React Native’s Accessibility API allows us to query the system’s accessibility status:

```javascript
AccessibilityInfo.fetch().done((enabled) => {
  this.setState({
    AccessibilityEnabled: enabled,
  });
});
```

We can then listen for accessibility status changes:

```javascript
componentDidMount: function() {
  AccessibilityInfo.addEventListener(
    'change',
    this._handleAccessibilityChange
  );
  ...   
},

_handleAccessibilityChange: function(isEnabled: boolean) {
  this.setState({
    AccessibilityEnabled: isEnabled,
  });
},
```

With these APIs, our product teams can then toggle touch actions based on the system’s current accessibility info. For example, in the screenshot above, there are a lot of switches to toggle push notifications. When someone is using a screen reader, we can then read out the entire information in the row, including the toggle and state, e.g., “Ad Approved, Status On” — the user can then toggle the status by double tapping the highlighted area, e.g., double tap the row.

```javascript
var onSwitchValueChange = this.props.onValueChange;
var onRowPress = null;
if (this.state.isAccessibilityEnabled) {
  onSwitchValueChange = null;
  onRowPress = this.props.onValueChange;
}

var switch = <Switch onValueChange={onSwitchValueChange} ... />
return
  <InfoRow
    action={switch}
    onPress={onRowPress}
    ...
  />
```

React Native provides a powerful way for you to build applications on iOS and Android, and it enables efficient reuse of code. With the React Native Accessibility API, you can make sure the great experiences you are creating will be usable by people with disabilities and other users of assistive technology.

For more information on the React Native AX API, check out our [developer documentation](https://facebook.github.io/react-native/docs/accessibility.html).
