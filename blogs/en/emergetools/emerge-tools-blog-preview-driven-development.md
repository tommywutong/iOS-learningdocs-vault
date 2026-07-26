---
title: 'Emerge Tools Blog | Preview Driven Development'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/preview-driven-development'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c1a392aa15a49525'
translated: false
---

> 原文：[Emerge Tools Blog | Preview Driven Development](https://www.emergetools.com/blog/posts/preview-driven-development)　·　Emerge Tools Blog

# Preview Driven Development

October 30, 2024 by

Rikin Marfatia & Ryan Brooks

AndroidSnapshot Testing

![Preview Driven Development](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.0df5ce31.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Previews are, hands down, my favorite feature of Compose. They are amazing as a tool for building UIs, but they can be **so much more** than that. While building our [Hacker News](https://play.google.com/store/apps/details?id=com.emergetools.hackernews&hl=en-US&ah=nDI5tSolFhFSYhq9lXsI98VgwsQ) client, we used Previews as a core part of our workflow. We're calling this approach: Preview-Driven Development.

Fundamentally, it's a combination of two ideas:

1. Previews can act as tests to maintain app quality
2. Previews can be mini-apps to launch features in controlled environments

We'll explore these concepts through real examples we faced while building Hacker News. Then, we'll build upon these ideas by introducing automation and transforming our previews into a robust suite of snapshot tests backed by our CI solution.

## [Previews vs. Tests](https://www.emergetools.com/blog/posts/preview-driven-development#previews-as-tests)

One thing we wanted to explore as we were building Hacker News was different ways of ensuring the app behaved correctly. Typically, we might reach for Unit and Integration Tests here, but we were interested in using Previews for this need.

This isn't a random idea. Emerge has a [Snapshot Testing](https://docs.emergetools.com/docs/snapshot-testing) tool that leverages Previews to generate snapshot tests. These tests verify everything works by seeing snapshots of what is rendered. As a unit test replacement, there are some interesting benefits — namely, the output is the real screen/feature/component that users will see.

### [Fixing a Crash](https://www.emergetools.com/blog/posts/preview-driven-development#fixing-a-crash)

Soon after we launched our Hacker News app, we checked Sentry and noticed that a crash had slipped through the cracks. Turns out, we were incorrectly parsing timestamps.

![Crash statistics showing multiple timestamp parsing crashes](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog28%2Fcrash-stats.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Yikes…that's a lot of crashes

The issue was around parsing ISO timestamps, _sometimes_ with timezone data included, as a `LocalDateTime` without giving it the proper formatter. It was difficult to reproduce organically and we couldn't always find a post that would cause a crash. However, we _did_ know what component and date type could cause it. That's when we decided to use a Preview to quickly repro the issue, and it worked great!

The offending component was our `CommentRow`, which tries to parse the comment timestamp and convert it into a relative time label. So we set up our failing _Test Case Preview_ as follows:

```kotlin
@Preview
@Composable
private fun TestIsoDateTimeParsing() {
  HackerNewsTheme {
    Column {
      val isoDateWithTimeZone = "2024-09-05T17:48:25.000000Z"
      CommentRow(
        state = CommentState.Content(
          id = 1,
          author = "rikinm",
          content = "Hello Parent",
          age = isoDateWithTimeZone,
        ),
        onToggleHide = {},
        onLikeTapped = {}
      )
    }
  }
}

@Composable
fun CommentRow() {
  // ...
  MetadataTag(
    label = relativeTimeStamp(state.age),
  ) {
    //...
  }
}

fun relativeTimeStamp(date: String): String {
  val dateEpochs = LocalDateTime.parse(date)
    .toInstant(ZoneOffset.UTC)
    .epochSecond
  val now = Instant.now().epochSecond
  val difference = now - dateEpochs

  val minutes = difference / SECONDS_IN_MINUTE
  if (minutes < 60) {
    return "${minutes.toInt()}m ago"
  }

  val hours = minutes / MINUTES_IN_HOUR
  if (hours < 24) {
    return "${hours.toInt()}h ago"
  }

  val days = hours / HOURS_IN_DAY
  return "${days.toInt()}d ago"
}
```

Sure enough, the Preview wouldn't render, and we saw the same crash.

![Preview showing a crash in Android Studio](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog28%2Fpreview-crashing.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The fix was pretty straightforward (and our [first open-source contribution](https://github.com/EmergeTools/hackernews/pull/136), thanks Ed!). We just needed to add `DateTimeFormatter.ISO_DATE_TIME` to help us optionally parse time zone data if it exists.

```kotlin
fun relativeTimeStamp(date: String): String {
  val dateEpochs = LocalDateTime
    .parse(date, DateTimeFormatter.ISO_DATE_TIME)
    .toInstant(ZoneOffset.UTC)
    .epochSecond
  //...
}
```

![Fixed preview showing correctly parsed timestamp](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog28%2Ffixed-preview.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

We're back in working order, and now this Preview serves as a test to ensure we handle timestamps correctly. We don't need a separate Test class, and our Preview is right next to the actual component. We can verify correctness on the rendered component, rather than creating a variety of test assertions. And as we'll cover later, we can easily create tests around the working Preview to ensure a future change doesn't break it.

### [Handling Edge Cases](https://www.emergetools.com/blog/posts/preview-driven-development#handling-edge-cases)

Here's our roadmap on how to create Preview-based testing:

1. Determine the component and behavior you want to test
2. Construct a UI state that will exercise that behavior
3. See what's rendered in your Preview

There are some levers you can pull, but this is the crux of it. We used this technique to help us diagnose and fix that crash, but more often we use it to test various edge cases we want our UI to handle.

It's not uncommon to forget about some of these "unhappy paths", ignoring how our component handles error, loading, or empty states. To combat this, we can preemptively create Previews that exercise these conditions so that we have a visual reminder that they are not being handled and will be seen by users if that's the case.

For our Bookmarks Feature, we constructed an empty state Preview, which is likely what users will see when interacting with it for the first time.

```kotlin
@SnapshotPreview
@Composable
fun BookmarksScreenEmptyPreview() {
  HackerNewsTheme {
    BookmarksScreen(
      state = BookmarksState(
        bookmarks = emptyList()
      ),
      actions = {},
      navigator = {}
    )
  }
}
```

![Empty state preview of the Bookmarks screen](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog28%2Fempty-states.jpg&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

This meant we had an explicit visual reminder that if we ignored that case users would see a very blank and empty screen. We made sure to fill this with some education to fill the void and teach users how to bookmark stories. This worked for things like loading and error states, getting visual reminders to make sure we handled those cases as well.

To reiterate the benefits here:

- It's really easy to set up this "Preview Test" and even co-locate it with the component being tested (especially in an LLM world)
- The output is visual, we can actually see the component we are testing render which is also exactly what users would see as well

## [Previews as Mini Apps](https://www.emergetools.com/blog/posts/preview-driven-development#previews-as-mini-apps)

The idea of mini-apps is the ability to launch each feature as an app in a controlled environment. The last part is important. Having control over the environment means not being blocked by internet outages, easily testing loading and error states, and even [reducing build times](https://code.cash.app/attacking-build-times-with-sample-apps).

Previews make this setup trivial. By adding our logic layer and stubbing out dependencies with fakes, our **Feature Previews** can become functional mini-apps that can dynamically exercise the actual logic of our feature. For Hacker News, we used this to iterate on the Stories Feed. Let's go through the setup:

```kotlin
class StoriesViewModel(  
  private val baseClient: BaseClient,  
  private val bookmarkDao: BookmarkDao  
) : ViewModel() {  
  private val internalState = MutableStateFlow(StoriesState(stories = emptyList()))  
  val state = internalState.asStateFlow()
  // omitted
```

Our `StoriesViewModel` is our logic layer for the Stories Feed, and if we want to use it in our Feature Preview we have to control its dependencies and use Fakes instead. What this means in practice is looking at our dependency, and extracting out an interface with its core API.

```kotlin
interface BaseClient {  
  suspend fun getFeedIds(type: FeedType): FeedIdResponse  
  suspend fun getPage(page: Page): List<Item>  
  suspend fun getItem(itemId: Long): ItemResponse  
}

class RealBaseClient(  
  json: Json,  
  client: OkHttpClient,  
) : BaseClient {  
  private val retrofit = Retrofit.Builder()  
    .baseUrl(BASE_FIREBASE_URL)  
    .addConverterFactory(json.asConverterFactory("application/json; charset=UTF8".toMediaType()))  
    .client(client)  
    .build()  
  
  private val api = retrofit.create(HackerNewsBaseApi::class.java)  
  
  override suspend fun getFeedIds(type: FeedType): FeedIdResponse {  
    // code
  }  
  
  override suspend fun getPage(page: Page): List<Item> {  
    // code
  }  
  
  override suspend fun getItem(itemId: Long): ItemResponse {  
    // code
  }  
}
```

Once we've done that, we can start creating Fakes that implement the interface and return static responses. We'll pass these fakes into the ViewModel when it's used in a FeaturePreview.

```kotlin
class FakeBaseClient : BaseClient {  
  private val fakeItems = listOf(  
    Item(  
      id = 1L,  
      type = "story",  
      title = "Launch HN: Airhart Aeronautics (YC S22) – A modern personal airplane",  
      by = "heyrikin",  
      score = 252,  
      descendants = 229,  
      time = Instant.now().epochSecond,  
    ),
    // more items
  )
      
  override suspend fun getFeedIds(type: FeedType): FeedIdResponse {  
    return FeedIdResponse.Success(  
      page = fakeItems.map { it.id }  
    )  
  }
    
  override suspend fun getPage(page: Page): List<Item> {  
    delay(1000) // artificial delay for loading
    return fakeItems  
  }  
  
  override suspend fun getItem(itemId: Long): ItemResponse {  
    return fakeItems.first { it.id == itemId }  
  }  
}

@Preview  
@Composable  
private fun StoriesScreenFeaturePreview_Normal() {  
  HackerNewsTheme {  
    val model = remember {  
      StoriesViewModel(  
        baseClient = FakeBaseClient(),  
        bookmarkDao = FakeBookmarkDao()  
      )    
    }  
    val state by model.state.collectAsState()  
    
    StoriesScreen(  
      state = state,  
      actions = model::actions,  
      navigation = {}  
    )  
  }  
}
```

With this setup, we now have a functional Feature Preview of the Stories Feed. We can even verify loading states by adding some artificial delay to simulate network conditions.

To verify error states, we can create a new Fake that returns Errors instead and use that Fake in another Feature Preview.

```kotlin
class ErrorBaseClient : BaseClient {  
  override suspend fun getFeedIds(type: FeedType): FeedIdResponse {  
    delay(1000) // artificial delay
    return FeedIdResponse.Error("⛔️ Uh-oh")  
  }  
  override suspend fun getPage(page: Page): List<Item> {  
    throw NotImplementedError("Should not call this function")  
  }  
  override suspend fun getItem(itemId: Long): ItemResponse {  
    throw NotImplementedError("Should not call this function")  
  }
}

@Preview  
@Composable  
private fun StoriesScreenFeaturePreview_Error() {  
  HackerNewsTheme {  
    val model = remember {  
      StoriesViewModel(  
        baseClient = ErrorBaseClient(),  
        bookmarkDao = FakeBookmarkDao()  
      )    
    }  
    val state by model.state.collectAsState()
      
    StoriesScreen(  
      state = state,  
      actions = model::actions,  
      navigation = {}  
    )  
  }  
}
```

The key difference between this and a static Preview with a constructed error state passed is that this Feature Preview actually exercises our logic. It reaches into the `ViewModel`, hits the data source, and flows through the same areas our real application would.

### [Improving Build Times](https://www.emergetools.com/blog/posts/preview-driven-development#improving-build-times)

If you really lean into Feature Previews, you can develop a simple modularization strategy and create mini-apps that are fast to build.

![An example module structure that allows for fast previews](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog28%2Fsimple-module-structure.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The idea is that your interface and real implementation of a dependency should be in separate modules. This allows your Feature module to only bring in the interface module, which can host your Fakes as well. Then, you can create a Feature Preview module, which is an application module that only depends on the Feature and only brings in Fakes. This will allow your Feature Previews to build and launch really fast.

Don't just take our word for it; [check out Ralf](https://www.droidcon.com/2019/11/15/android-at-scale-square/) talking about Square's experience with a similar approach. This example is a bit older and doesn't use Previews, but it shows a similar structure to launching mini-apps. In their case, they consistently built in **under 10 seconds** vs. the **3-4 minute** build time of the live path.

## [Automating PDD](https://www.emergetools.com/blog/posts/preview-driven-development#automating-pdd)

We covered the local benefits of PDD, now let's take it a step further. We want to ensure our previews are checked on every commit or PR and that we are alerted if anything breaks or changes. Here's some things we might need:

- Continuously running Previews and capturing the output
- A history of previous runs and captures
- UI to see visual diffs between current capture and the baseline
- Image storage, since our output is an image

This is not trivial to systematize. If you prefer a much simpler path, you can use Google's own [screenshot testing tool](https://developer.android.com/studio/preview/compose-screenshot-testing) or [Emerge Snapshots](https://www.emergetools.com/product/snapshots). With Emerge, your Previews automatically become a **powerful** Snapshot test suite with a dashboard to see all test results and visual diffs.

All you need to do is add the Gradle plugin and Snapshot SDK and then run the provided Gradle task to generate and upload new snapshots.

### [A Basic CI Setup](https://www.emergetools.com/blog/posts/preview-driven-development#basic-ci-setup)

Hacker News has a very simple CI implementation to incorporate Snapshots. We leverage Emerge's Gradle Plugin for most of the heavy lifting and use Github Actions to trigger Snapshot updates. It allows for a system that uploads snapshots on new PRs so they can be verified before merging changes.

⚙️

You can check out HackerNews implementation for the [Gradle Plugin](https://github.com/EmergeTools/hackernews/blob/2cc224a3ee355f4b0044bbae74b20b6a3f820dd7/android/app/build.gradle.kts#L90) and [Github Actions](https://github.com/EmergeTools/hackernews/blob/2cc224a3ee355f4b0044bbae74b20b6a3f820dd7/.github/workflows/android_emerge_snapshots.yml#L1)

Anytime a PR is opened against main, we generate snapshots and compare them to our current base build. If there are any changes, we get a comment on our PR and a status check.

![A status check showing snapshot test results](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog28%2Fstatus-check.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools Snapshot status check

We can then go to the Emerge Tools dashboard to see any added, changed, or failed snapshot tests. If we're happy with the changes, we can approve them from this dashboard and the status check will now pass.

With a little bit setup, we now have a robust system around our Preview-based snapshots to help us guard against any visual or logical regressions.

## [Conclusion](https://www.emergetools.com/blog/posts/preview-driven-development#conclusion)

PDD is a bet on Previews. They shouldn't be an afterthought; rather, they should be thought about and used early in your workflow. They can be powerful tests that help you maintain app quality and can be used as functional mini-apps that allow you to build your features quickly in controlled environments.

These ideas aren't all new either. Check out some of these resources that talk about similar use cases for Previews:

- [Preview Driven Development](https://www.youtube.com/watch?v=cKfTx3AxChA&t=1431s)- Rikin @ Android Worldwide
- [Composable Preview Driven Development](https://www.youtube.com/watch?v=cDqdosrS83k)- Sergio @ Droidcon Lisbon

Even Google is investing heavily in Previews by creating its own Screenshot testing solution. We believe that this is the way to build high-quality Compose apps at scale.

Thanks for reading, don't forget to check out [Hacker News](https://play.google.com/store/apps/details?id=com.emergetools.hackernews&hl=en-US&ah=nDI5tSolFhFSYhq9lXsI98VgwsQ) (it's [open source](https://github.com/EmergeTools/hackernews) btw 🤓).
