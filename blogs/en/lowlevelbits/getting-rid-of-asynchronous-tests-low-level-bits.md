---
title: Getting Rid of Asynchronous Tests - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/getting-rid-of-asynchronous-tests/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:993be35a8e3bc248'
translated: false
---

> 原文：[Getting Rid of Asynchronous Tests - Low Level Bits 🇺🇦](https://lowlevelbits.org/getting-rid-of-asynchronous-tests/)　·　Low Level Bits (Alex Denisov)

# Getting Rid of Asynchronous Tests

_Published on Jun 17, 2015_

### Asynchronous tests are not reliable

So you’re working on your Cocoa/CocoaTouch app and find yourself having to write tests for your network layer. You’re using the NSURLSession API and now you have to take asynchrony into account while TDDing around. You don’t want your specs making network calls, so you go for a tool like [Nocilla](https://github.com/luisobo/Nocilla) and [OHHTTPStubs](https://github.com/AliSoftware/OHHTTPStubs).

While these tools are really great, whether you know it or not, they throw you into the nondeterministic world of NSRunLoop-related shared and unmanaged state. That is, your tests may pass for most of the time, but fail randomly once in a while, leaving you with no easy way to find out why. Put more simply: **asynchronous tests are unreliable**.

### Getting rid of asynchrony

To make those tests reliable we need to get rid of asynchrony. There are a few frameworks that simplify this task, like: [OCMock](http://ocmock.org), [OCMockito](https://github.com/jonreid/OCMockito) or [Cedar](https://github.com/pivotal/cedar).

As big fan of ObjC++, I’ll go with Cedar, but any one of the above can get the job done.

Let’s first consider the components of a system under test:

`Loader` - loads raw `NSData` from the network or returns an error

`Client` - handles error/raw data from the `Loader` and sends it to an end user

Here is the interface of the `Loader`:

```objective
@interface Loader : NSObject

- (void)loadDataWithCompletion:(void (^) (NSData *data, NSError *error))completion;

@end
```

the interface of the `Client`

```objective
typedef void (^Callback) (NSArray *users, NSError *error);
@class Loader;

@interface Client : NSObject

@property Loader *loader;

- (void)loadUsersWithCallback:(Callback)callback;

@end
```

and it’s implementation:

```objective
@implementation Client

- (void)loadUsersWithCallback:(Callback)callback {
  [self.loader loadDataWithCompletion:^(NSData *data, NSError *error) {
    NSArray *users = parseUsers(data);
    NSError *finalError = processError(error);
    callback(users, finalError);
  }];
}

@end
```

Our goal is to test that the client parses data and handles errors in a correct way:

```objective
describe(@"Client", ^{
  Client *client = [Client new];

  it(@"should parse data", ^{
    NSArray *expectedUsers = ethalonUsers();
    NSArray *actualUsers = nil;

    [client loadUsersWithCallback:^(NSArray *users, NSError *error) {
      actualUsers = users;
    }];

    actualUsers should equal(expectedUsers);
  });

  it(@"should process error", ^{
    NSError *expectedError = ethalonError();
    NSError *actualError = nil;

    [client loadUsersWithCallback:^(NSArray *users, NSError *error) {
      actualError = error;
    }];

    actualError should equal(expectedError);
  });

});
```

To test this we just need to replace the `client.loader` with a fake object that is going to mimic the desired behavior.

Here is how it looks like with Cedar:

```objective
typedef void (^LoaderCallback)(NSData *data, NSError *error);

// parse data
SEL sel = @selector(loadDataWithCompletion:);
Loader *loader = fake_for(Loader.class);
loader stub_method(sel).and_do(^(NSInvocation *invocation) {
  LoaderCallback callback = nil;
  NSData *data = getUsersData();
  [invocation getArgument:&callback atIndex:2];
  callback(data, nil);
});

// parse data
SEL sel = @selector(loadDataWithCompletion:);
Loader *loader = fake_for(Loader.class);
loader stub_method(sel).and_do(^(NSInvocation *invocation) {
  LoaderCallback callback = nil;
  NSError *error = getError();
  [invocation getArgument:&callback atIndex:2];
  callback(nil, error);
});
```

For those unfamiliar with [`NSInvocation`](https://developer.apple.com/library/prerelease/ios/documentation/Cocoa/Reference/Foundation/Classes/NSInvocation_Class/index.html) let me cite it’s documentation:

```objective
/*
buffer:
  An untyped buffer to hold the returned argument. See the discussion below relating to argument values that are objects.

index:
  An integer specifying the index of the argument to get.
  Indices 0 and 1 indicate the hidden arguments self and _cmd, respectively; these values can be retrieved directly with the target and selector methods. Use indices 2 and greater for the arguments normally passed in a message.
*/
- (void)getArgument:(void * nonnull)buffer atIndex:(NSInteger)index;
```

After putting these parts together you’ll have this cryptic code:

```objective
typedef void (^LoaderCallback)(NSData *data, NSError *error);

static Loader *fakeUsersLoader() {
  SEL sel = @selector(loadDataWithCompletion:);
  Loader *loader = fake_for(Loader.class);
  loader stub_method(sel).and_do(^(NSInvocation *invocation) {
    LoaderCallback callback = nil;
    NSData *data = getUsersData();
    [invocation getArgument:&callback atIndex:2];
    callback(data, nil);
  });
}

static Loader *fakeErrorLoader() {
  SEL sel = @selector(loadDataWithCompletion:);
  Loader *loader = fake_for(Loader.class);
  loader stub_method(sel).and_do(^(NSInvocation *invocation) {
    LoaderCallback callback = nil;
    NSError *error = getError();
    [invocation getArgument:&callback atIndex:2];
    callback(nil, error);
  });
}

describe(@"Client", ^{
  Client *client = [Client new];

  it(@"should parse data", ^{
    client.loader = fakeUsersLoader();

    NSArray *expectedUsers = ethalonUsers();
    NSArray *actualUsers = nil;

    [client loadUsersWithCallback:^(NSArray *users, NSError *error) {
      actualUsers = users;
    }];

    actualUsers should equal(expectedUsers);
  });

  it(@"should process error", ^{
    client.loader = fakeErrorLoader();

    NSError *expectedError = ethalonError();
    NSError *actualError = nil;

    [client loadUsersWithCallback:^(NSArray *users, NSError *error) {
      actualError = error;
    }];

    actualError should equal(expectedError);
  });
});
```

### Summary

One of our modules had lots of asynchronous network tests which were failing randomly. As you might imagine, that’s not an optimal situation to find yourself in. By getting rid of asynchrony, we didn’t only get rid of random failures, but also decreased execution time from ~2.5s to ~0.01s.

Have fun writing those reliable, deterministic tests!
