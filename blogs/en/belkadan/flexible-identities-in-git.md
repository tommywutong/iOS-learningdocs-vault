---
title: Flexible Identities in git
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/'
original_language: en
published: 2020-02-06
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:95451e9f7b965dc6'
translated: false
---

> 原文：[Flexible Identities in git](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/)

[Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/) »

« [Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=git)

[Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=git) »

« [Pronoun Buttons](https://belkadan.com/blog/2016/06/Pronoun-Buttons/?tag=diversity-in-tech)

## [Flexible Identities in git](#)

> Noticed a colleague changed their name from traditionally-gender-A to tradtiionally-gender-B, and so went to clean up my comments of the form "thanks, [name]" to just "thank you".  
>   
> Doesn't really hide anything, but at the very least they won't be deadnamed if looking at old PRs?
> 
> — Jordan Rose (@UINT_MIN) [April 13, 2019](https://twitter.com/UINT_MIN/status/1116926726980820992?ref_src=twsrc%5Etfw)

> Git is terrible for this sort of identity-severing change thanks to burning the committer's name into the validity of the branch, and we-the-industry should probably do something.
> 
> — Jordan Rose (@UINT_MIN) [April 13, 2019](https://twitter.com/UINT_MIN/status/1116926727647707136?ref_src=twsrc%5Etfw)

At the time, I decided to play with this a bit. Git is famous for preserving history as hard as possible—not just in commits having a link to their parent, but also in keeping around the local history of branches _even when you reset them._ So I came up with three criteria:

1. Changing name does not affect existing history
2. Changing name does not leave old name in repo anywhere
3. `git fetch` will get new names without `--force`

And of course this should all work with plain old git.

## Aside: Why?

As far as I know, trans people have the only significant use for “I changed my name so hard I want to bury my old one, but I still want to stay attached to the things I did under my old name”. Other name changes usually aren’t in this sweet spot: changes due to marriage, adoption, etc are important, but usually not to the point that you mind people seeing your old name; and changes due to abandoning a previous identity (witness protection?) would usually mean you don’t want to be associated with your old work.

It’s worth noting that the “benign” case here is already handled by [mailmaps](https://www.git-scm.com/docs/git-shortlog#_mapping_authors). Mailmaps are also useful if you’ve changed email providers for whatever reason. (A downside of mailmaps is that they’re part of the repository, so if you check out an old commit you’ll have an old mailmap too.)

But even though there’s only one use case for this today, it’s an important one. “[Deadnaming](https://www.healthline.com/health/transgender/deadnaming)” someone who’s trans, even unwittingly, can stir up [dysphoria](https://www.healthyplace.com/blogs/thelifelgbt/2019/3/gender-dysphoria-vs-transgender-identity), feel like disrespect, and/or expose them to discrimination by outing them as trans, just like [using the wrong pronouns](https://belkadan.com/blog/2016/06/Pronoun-Buttons/). Git is software that doesn’t account for this and so we should do better.

I’m not trans myself, and I probably won’t be pushing for this outside of this post. And I’m not going to pretend that my attempt here is some kind of selfless, praiseworthy effort. I wanted to see if it was _possible_ to do this; that’s all. But it _is_ something to think about when designing a successor to git.

## Initial Solution: Custom Refs

> _[We can solve any problem by introducing an extra level of indirection.](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering)_

[The first solution I came up](https://twitter.com/UINT_MIN/status/1120552520538042368) with _mostly_ satisfies the original criteria.

1. Pick a unique identifier; let’s call it `IDENT`. (We’ll come back to this later.)
2. Change your user information to refer to that identifier, and make it clear you’re hiding your info.

  ```
  git config user.name "refs/authors/$IDENT"
  git config user.email ""
  ```
3. Write your name directly into the git repository using [`git hash-object`](https://www.git-scm.com/docs/git-hash-object).

  ```
  INFO=$(echo "Lovelace <ai@example.com>" | git hash-object -w --stdin)
  ```
4. Record that object with a custom _ref,_ named after your unique identifier, using [`git update-ref`](https://git-scm.com/docs/git-update-ref). (This is why the fake name above started with “refs/”.)

  ```
  git update-ref refs/authors/$IDENT "$INFO"
  ```
5. Push the author ref.

  ```
  git push origin refs/authors/$IDENT
  ```

A [custom ref](https://git-scm.com/book/en/v2/Git-Internals-Git-References) is like a tag in that it can point to files (blobs) as well as commits, but crucially git won’t try to protect it from being updated if you fetch it and it’s changed. We also don’t really want these to show up in the repo’s list of tags.

On the client side, you _do_ have to fetch an author’s name to see it. The dummy name in a commit will at least tell you what to fetch.

```
git fetch origin refs/authors/$IDENT
git show refs/authors/$IDENT
```

When you do decide to change your name, you do it the same way as before—steps 3-5—except it’ll be a force push.

```
INFO=$(echo "Sidra <sidra@example.com>" | git hash-object -w --stdin)
git update-ref refs/authors/$IDENT "$INFO"
git push --force origin refs/authors/$IDENT
```

### The Good

> Changing name does not affect existing history

Accomplished!

> Changing name does not leave old name in repo anywhere

90% accomplished. There are no _references_ to the old name in the repo, and new cloners won’t have access to it, but existing repos will still have the old name _somewhere_ until [git garbage collection](https://git-scm.com/docs/git-gc) runs. I think this is acceptable; it’s very very rare that someone would go groveling through the random objects in their git repo that aren’t connected to any branch or tag or other ref. We’re not really trying to stop bad actors _trying_ to deadname someone, just keeping it from happening accidentally.

> `git fetch` will get new names without `--force`

Technically accomplished (the best kind of accomplished?). [`git fetch` will not require `--force` to update refs that aren’t branches or tags](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-ltrefspecgt)…but at the same time, it won’t fetch updates at all if you don’t ask for them. Which brings us to…

### The Not-So-Good

**There’s no indication whether an author ref is up to date.** To be sure, you’d have to fetch the ref again. A better choice would be to set the default behavior of `git fetch` to include “author refs”.

```
git config --add remote.$NAME.fetch 'refs/authors/*:refs/authors/*'
```

This is non-wonderful. It’s something the _client_ has to set up, not the person with the flexible name. To add insult to injury, it has the name of the remote in it, so it’s not just something that can be copy/pasted. Good thing most people use “origin”.

This drawback has me going back and forth about whether the “name” field really _should_ have “refs” in it. It might be better to have it just be “authors/IDENT” part, possibly with some kind of prefix, and the “email” field could be something like “flexiblegit.net” that explains all this.

Separately, **anyone with commit access can change someone else’s name.** I don’t know _why_ someone might want to do this, but since we’re _explicitly not recording history_ it’d be hard to undo. It might even be hard to _notice._

```
INFO=$(echo "Zoosmell Pooplord <ectobiologist@example.com>" | git hash-object -w --stdin)
git update-ref refs/authors/$SOMEONE_ELSE "$INFO"
git push --force origin refs/authors/$SOMEONE_ELSE
```

Finally, **it’s annoying to have to look up people’s names in two steps.** Can we get `git log` and friends to do the lookup for us?

I don’t have an answer to the first problem, but I do have ideas for the second and third.

## Signing your name

…I’m referring to [digital signatures](https://en.wikipedia.org/wiki/Digital_signature), of course.

*cough*

What we want is a way to say “IDENT belongs to me” in a way that doesn’t actually reveal who this “me” is, and that’s what digital signatures do. “Given a public key, we can verify that this content was generated by the person with the corresponding private key.”

I haven’t fully worked out the details here, but it looks something like this:

1. Write your _public key_ directly into the repo, making sure _it_ doesn’t have any identifying info. _That hash is your unique identifier._

  ```
  IDENT=$(gpg --armor --export | git hash-object -w --stdin)
  ```
2. To make sure the public key doesn’t get garbage-collected, it needs to be attached to some kind of ref. To accomplish that, we’ll have our author ref point to a _tag_ object, which will then point to the public key. Unfortunately, this has to be done in sort of a clunky way:

  ```
  git tag name $IDENT \
    -m 'Lovelace <ai@example.com>' \
    -m "$(echo 'Lovelace <ai@example.com>' | gpg --detach-sig --armor)"

  git update-ref refs/authors/$IDENT name

  # Delete the 'name' tag (no longer needed)
  git tag -d name
  ```

  And because that’s a bit of a mess, it’d probably be worth writing a helper script to do it, but that’s not too hard.

  _EDIT: Changed hypothetical `sign` invocation to an actual `gpg` invocation that works, thanks to [a tip from Jon Roelofs](https://twitter.com/jon_roelofs/status/1227580129053855745)._
3. Push and `show` the ref as usual.

  ```
  git push origin refs/authors/$IDENT

  git fetch
  git show refs/authors/$IDENT
  ```

What you get back would look like this:

```
tag name
Tagger: authors/$IDENT <>
Date:   Wed Feb 5 11:22:33 2020

Lovelace <ai@example.com>

---BEGIN SIGNATURE---
some gobbledygook here
---END SIGNATURE---
---BEGIN PUBLIC KEY---
more gobbledygook here
---END PUBLIC KEY---
```

…with the tag’s metadata, then its message—the name and the signature—then the contents of the thing it refers to: your public key. A human can pick out the important bit—your name—but also all the information’s there to verify that it was you who made the tag, because…

- …whoever made the tag signed it with…
- …the private key that matches the public key it refers to…
- …whose hash is part of the name of the tag.

Once again, changing your name is “easy”: repeat steps 2 and 3. You never actually check in a new “blob” object; you just make new tag objects. Which are not quite the same as tags.

Does this seem overly complicated? Another option would just be to make a normal “tree” (directory structure) containing your name, your public key, and your signature. I don’t love that either though: it makes things harder on clients, who can’t just say `git show` to see your name.

As with everything, there’s also a functionality tradeoff: if you ever lose your private key, you lose your identity. Someone _else_ can change your tag on your behalf, of course, but can other people trust that you wanted them to?

This is, of course, the feature we were after, but it may not be worth the trouble.

## Avoiding manual lookup

> _[We can solve any problem by introducing an extra level of indirection…except for the problem of too many levels of indirection.](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering)_

These solutions may accomplish our original goals, or close enough anyway, but they’re kind of a pain to use. Can we do better? My answer: **yes**, but it’s gonna be ugly.

Remember I talked about [mailmaps](https://www.git-scm.com/docs/git-shortlog#_mapping_authors) way back in the beginning? That’s the functionality we need: mapping names in commits to names suitable for display. But we need to make sure we’re not _storing_ the contents of the mailmap in the repository, or else we’d be back to where we started. Hmm…does git have any functionality for having the contents of the working directory be different from the contents of the repository itself?

[It totally does.](https://www.juandebravo.com/2017/12/02/git-filter-smudge-and-clean/)

In a nutshell, git allows you to set “smudge” and “clean” filters for processing files as they move in and out of git’s purview. (You should click through on that link above and scroll down to the bottom, where there’s a helpful diagram.) This is _supposed_ to be used for transformations that just affect that file, but…turns out…

…commands that invoke git also work. Which means we can check in a mailmap file like this:

```
refs/authors/IDENT <>
```

…and when it gets checked out it’ll look like this:

```
Sidra <sidra@example.com> refs/authors/IDENT <>
```

And now any commit with a name of “refs/authors/IDENT” and an empty email will be replaced by the right name when you do `git log`.

Here’s the opposite filter, by the way:

You need this to avoid checking in the names that were generated, which, again, would defeat the purpose.

The last piece of this is about forcing the mailmap to be updated. After all, git will only run these filters when something changes, either locally (an edit) or in the repository. So there’s one more step for adding or changing a name now: change the mailmap file at the root of the repository and commit it. Even if it’s just bumping a counter. (The first time you’ll be adding your name, but later on you’ll just have to make a dummy change.) That’s still not perfect, but it’ll at least be updated whenever someone updates their current branch—and that applies going forward _or_ backward.

This isn’t perfect. It’s brittle, it’s slightly abusing a git feature, and it requires a pile of client-side setup. But it’s _possible_ with just normal git.

## Conclusions

1. Git is very good at preserving history, but we can circumvent that using custom refs.
2. Therefore, we can build a “flexible name” system on the git we have today.
3. But usability leaves a lot to be desired…
4. …and authentication (signing) is messy, doubly so because tools don’t work the way I think they should. (I’m not a cryptographer so I’m probably wrong.)

This was a good exercise, but I don’t know if it’s something that would really be viable anywhere. Still, now it’s out there and people can refer to it. (Let me know what you think on Twitter.)

This entry was posted on [February](https://belkadan.com/blog/2020/02) 06, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git), [Diversity in tech](https://belkadan.com/blog/tags/diversity-in-tech)
