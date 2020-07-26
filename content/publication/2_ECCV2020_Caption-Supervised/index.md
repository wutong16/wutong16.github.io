---
title: "Caption-Supervised Face Recognition: Training a State-of-the-Art Face Model without Manual Annotation"
authors:
# - Qingqiu Huang
# - Lei Yang  
# - Huaiyi Huang
# - Tong Wu
# - Dahua Lin
date: "2020-07-03"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-07-01T00:02:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *European Conference on Computer Vision (ECCV)*
publication_short: In *ECCV*

abstract: The advances over the past several years have pushed the performance of face recognition to an amazing level. This great success, to a large extent, is built on top of millions of annotated samples. However, as we endeavor to take the performance to the next level, the reliance on annotated data becomes a major obstacle. We desire to explore an alternative approach, namely using captioned images for training, as an attempt to mitigate this difficulty. Captioned images are widely available on the web, while the captions often contain the names of the subjects in the images. Hence, an effective method to leverage such data would significantly reduce the need of human annotations. However, an important challenge along this way needs to be tackled, the names in the captions are often noisy and ambiguous, especially when there are multiple names in the captions or multiple people in the photos. In this work, we propose a simple yet effective method, which trains a face recognition model by progressively expanding the labeled set via both selective propagation and caption-driven expansion. We build a large-scale dataset of captioned images, which contain 6.3M faces from 305K subjects. Our experiments show that using the proposed method, we can train a state-of-the-art face recognition model without manual annotation (99.65% in LFW). This shows the great potential of caption-supervised face recognition.

# Summary. An optional shortened abstract.
summary: Accepted by European Conference on Computer Vision (ECCV), 2020 <br> *[Qingqiu Huang](http://qqhuang.cn/), [Lei Yang](https://github.com/yl-1993), [Huaiyi Huang](https://github.com/hahehi), **Tong Wu**, [Dahua Lin](http://dahua.me/)*


tags:
- Source Themes
featured: true

links:
url_pdf: '#'
url_code: '#'
url_slides: '#'
url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Overall framework'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: 


# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: 
---
<!-- 
{{% alert note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /alert %}}

{{% alert note %}}
Click the *Slides* button above to demo Academic's Markdown slides feature.
{{% /alert %}}

Supplementary notes can be added here, including [code and math](https://sourcethemes.com/academic/docs/writing-markdown-latex/). -->

