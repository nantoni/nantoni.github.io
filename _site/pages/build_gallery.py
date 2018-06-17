#! /usr/bin/python

f = open('./gallery_file.md', 'r')


column_1 = ""
column_2 = ""
column_3 = ""

switch = 1
count = 1


for line in reversed(list(f)):
    if count%3 == 0:
        pass
    elif count%3 == 1:
        alt = line
    else:
        src = line
        if switch == 1:
            column_1 = column_1 + """<div class="container">
  <img class="image" src=\"""" + src + """" style="width:100%" onclick="onClick(this)" alt=\"""" + alt + """">
</div>"""

            switch = 2
        elif switch == 2:
            column_2 += """<div class="container">
  <img class="image" src=\"""" + src + """" style="width:100%" onclick="onClick(this)" alt=\"""" + alt + """">
</div>"""
            switch = 3
        else:
            column_3 += """<div class="container">
  <img class="image" src=\"""" + src + """" style="width:100%" onclick="onClick(this)" alt=\"""" + alt + """">
</div>"""
            switch = 1
    count += 1

f.close()


gallery_html = """---
layout: default
---

<style>

* {
    box-sizing: border-box;
}

.row {
    display: flex;
    flex-wrap: wrap;
    padding: 0 4px;
}

/* Create 3 equal columns that sits next to each other */
.column {
    flex: 33.33%;
    max-width: 33.33%;
    padding: 0 4px;
}

.column img {
    margin-top: 8px;
    vertical-align: middle;
}

.image {
  opacity: 1;
  display: block;
  width: 100%;
  height: auto;
  transition: .2s ease;
}

.image:hover{
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)
}

.container:hover .image {
  cursor: pointer;
}

/* Responsive layout - makes a two column-layout instead of three columns */
@media (max-width: 800px) {
    .column {
        flex: 50%;
        max-width: 50%;
    }
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media (max-width: 600px) {
    .column {
        flex: 100%;
        max-width: 100%;
    }
}
</style>

<!-- Header -->
<header class="w3-container w3-center w3-padding-32">
  <h1><b>Gallery</b></h1>
  <p><a href="javascript:history.back()" class="w3-button w3-black">&laquo; BACK</a></p>
</header>

<!-- Grid -->
<div class="w3-row">

<!-- Post content -->
<div class="w3-col l8 s12">

  <!-- !PAGE CONTENT! -->
<div class="w3-main">

  <!-- Push down content on small screens -->
  <div class="w3-hide-large" style="margin-top:83px"></div>

  <!-- Photo Grid -->
  <div class="row" style="margin-top:8px" >
    <div class="column">
      """ + column_1 + """
    </div>
  <div class="column">
    """ + column_2 + """
    </div>
  <div class="column">
    """ + column_3 + """
    </div>
    </div>
  </div>
</div>
"""

# rewrite gallery.html

gallery = open('./gallery.html', 'w')

gallery.write(gallery_html)

gallery.close()
