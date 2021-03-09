---
title: "Towards Evaluating and Training Verifiably Robust Neural Networks"
authors: 
# - Tong Wu
# - Qingqiu Huang
# - Ziwei Liu # [Ziwei Liu](https://liuziwei7.github.io/)
# - Yu Wang
# - Dahua Lin
date: "2021-03-01"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-03-01T00:03:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*
publication_short: In *CVPR*

abstract: Recent works have shown that interval bound propogation (IBP) can be used to train verifiably robust neural networks. Reseachers observe an intriguing phenomenon on these IBP trained networks, CROWN, a bounding method based on tighter linear relaxation, often gives very loose bounds on these networks. We also observe that most neurons become dead during the IBP training process, which could hurt the representation capability of the network. In this paper, we study the relationship between IBP and CROWN, and prove that CROWN is always tighter than IBP when choosing appropriate bounding lines. We further propose a relaxed version of CROWN, linear bound propogation (LBP), that can be used to verify large networks to obtain lower verified errors than IBP. We also design a new activation function, parameterized ramp function (ParamRamp), which has more diversity of neuron status than ReLU. We conduct extensive experiments on MNIST, CIFAR-10 and Tiny-ImageNet with ParamRamp activation and achieve state-of-the-art verified robustness.

# Summary. An optional shortened abstract.
summary: Accepted by IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021, as **<font color='#FF5722'>Oral</font>** <br> *[Zhaoyang Lyu](https://github.com/ZhaoyangLyu), [Minghao Guo](https://www.minghaoguo.com/), **Tong Wu**, [Guodong Xu](https://xuguodong.netlify.app/), [Dahua Lin](http://dahua.me/)*

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

