---
title: "Distribution-Balanced Loss for Multi-Label Classification in Long-Tailed Datasets"
authors: 
# - Tong Wu
# - Qingqiu Huang
# - Ziwei Liu # [Ziwei Liu](https://liuziwei7.github.io/)
# - Yu Wang
# - Dahua Lin
date: "2020-07-04"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2020-07-03T00:03:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *European Conference on Computer Vision (ECCV)*
publication_short: In *ECCV*

abstract: We present a new loss function called Distribution-Balanced Loss for the multi-label recognition problems that exhibit long-tailed class distributions. Compared to conventional single-label classification problem, multi-label recognition problems are often more challenging due to two significant issues, namely the co-occurrence of labels and the dominance of negative labels (when treated as multiple binary classification problems). The Distribution-Balanced Loss tackles these issues through two key modifications to the standard binary cross-entropy loss, 1) a new way to re-balance the weights that takes into account the impact caused by label co-occurrence, and 2) a negative tolerant regularization to mitigate the over-suppression of negative labels. Experiments on both Pascal VOC and COCO show that the models trained with this new loss function achieve significant performance gains over existing methods.

# Summary. An optional shortened abstract.
summary: Accepted by European Conference on Computer Vision (ECCV), 2020, as **<font color='#FF5722'>Spotlightgit</font>** <br> ***Tong Wu**, [Qingqiu Huang](http://qqhuang.cn/), [Ziwei Liu](https://liuziwei7.github.io/), [Yu Wang](http://nicsefc.ee.tsinghua.edu.cn/people/yu-wang/), [Dahua Lin](http://dahua.me/)*

tags:
- Source Themes
featured: true

links:
url_pdf: https://arxiv.org/pdf/2007.09654.pdf
url_code: https://github.com/wutong16/DistributionBalancedLoss
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
{{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Click the *Slides* button above to demo Academic's Markdown slides feature.
{{% /callout %}}

Supplementary notes can be added here, including [code and math](https://sourcethemes.com/academic/docs/writing-markdown-latex/). -->

