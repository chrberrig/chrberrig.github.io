---
title: "I Finally Get Hugo"
date: 2024-12-16T16:50:45+01:00
draft: true
---

It took a lot of time, and my understanding is not complete, But I'm at the point where I *finally* sort of understand the HUGO SSG. 

So first of all, this entire site is build in Hugo. 
Directory structure is key to understand the framework of Hugo SSG. 
But this fact is presented up-front for everyone writing about this, and while this being an elegant solution that forces the site-creator to be fairly structured when making a website (since Hugo invites to a hierarchical tree-like structure similar to a directory structure), the syntax really don't help in this regard. 

As I'm not experienced in go-lang, this did not help. 
However I don't find my self overwhelmed by the syntax in Hugo, but rather by the referencing and scoping. 
The piece that finally made it click were the fact that I figured out the internal logic, connecting the idiosyncratic naming conventions, the scoping rules and directory structure. To my understanding this triplet makes the framework comprehensible. 

### In the beginning, there was the templates...

So the first thing that makes Hugo attractive as an SSG is the combination of making the majority of the writing in markdown (that needs a convention for commenting, Jesus H Christ... In Hugo however you can use HTML comments) OR using HTML, already here showing its flexibility. 
On the other hand, templating is done in HTML with the addition of some scoping into go. 

As an example, [this](https://github.com/chrberrig/smol/blob/ab87f41eb5a7c70ea73efebba3ed5f393e5dcaf5/layouts/_default/list.html) is the template that I use for "listings" of content in the lower hierarchical levels from a page. 

This is exemplary in the following ways:
- it clearly demonstrates the rules of scoping
- it shows how this plays together with the directory structure and the naming convention for Hugo. 

As the first point of order, note that just inside the main-tag, `{{ $listtitle := .Title }}` is written, which would be translated to:

"set the value of variable `listtitle` to `.Title`" where the .Title here refer to the title of the current list-page, as we have not entered into another scope as of yet. 
However, when we continue down the page and see the part saying:
```
{{ range .Sections }}
    <div class="subsection-summary">
        <h2><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
        {{ .Summary }}
    </div>
{{ end }}
```

Notice that we are, once again using the `.Title`, but this time, we have entered another scope, namely the *scope of all section-pages under the current page*, and only upon the end-statement, we exit back into the *current-page scope*. 

This tripped me up for a bit, because I nowhere could find this "implicit scoping rule" described. 

Contrast this to a language like Python, which makes the scoping explicit, even for the objects:

```
for object_element in list:
    object_element.apply_method()
```

In this case, you *explicitly* refer to the element in the list being looped over separating local from global naming. 

So with this implicit scoping in mind, our example from before suddenly become readable as:

**for each section under this page, make a heading consisting of the title of the section, make it a link and write its summary underneath. After this return to the scope of the current page**

While I see that this shorthand is quite effective, it requires a lot of implicit knowledge. 
I don't know if this is a go-lang thing or something specific to HUGO, but I can't help finding this implicit scoping bad form. 
It also might be that there are some traditions/convontions in web-dev that I am simply unaware of

With this knowledge we only need the diractory structure and the collections which is both tied to the naming conventions. 


<!-- TODO: something about looking at pre-made themes with these eyes for training -->
