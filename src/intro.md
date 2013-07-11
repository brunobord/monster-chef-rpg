Title: Introduction to yout project
Summary: Help page for the impatient

# Markdown

Here you can describe your project, using a simple Markdown file, and put
[links][link] and other cool markdown stuff.

This is a Github-flavored markdown parser, so you can add:

> Quotes to enhance your text.

or maybe code, if you like:

```python
print('hello world')
```

---

Tables are very very handy:

| Stuff      | Result                                  |
|:---------- |----------------------------------------:|
| Row 1      | These boots                             |
| Row 2      | are made                                |
| Other rows | for walking, and that all what they do  |

# Markdown extensions

This boilerplate project comes with handy extensions:

## Fragments

Put fragments that could be used more than once in your booklet, and "include"
them in several documents.

Step 1: put a file in your ``src/fragments`` directory. For example,
``fragment-test.md``. Edit its content, using the same Markdown syntax.

Step 2: add this line in a document:

```
~~fragment-test.md~~
```

This will add the fragment to the target document.

## Admonitions

You can add ReST-like admonitions this way:

```
    !!! note
        
        This is a note and this will be transformed into a "div.note" HTML tag
        container.
```

will be generated as:

!!! note
    
    This is a note and this will be transformed into a "div.note" HTML tag
    container.

Available pre-built admonitions:

* note
* rule
* info
* warning
* handwritten

You can add as many admonition as you want, you'll only have to define the CSS
look and feel in the `style.css` file. The sky is the limit.

[link]: https://github.com/
