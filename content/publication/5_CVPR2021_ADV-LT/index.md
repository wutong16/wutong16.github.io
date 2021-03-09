---
title: "Adversarial Robustness under Long-Tailed Distribution"
authors: 
# - Tong Wu
# - Qingqiu Huang
# - Ziwei Liu # [Ziwei Liu](https://liuziwei7.github.io/)
# - Yu Wang
# - Dahua Lin
date: "2021-03-02"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-03-02T00:03:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: In *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*
publication_short: In *CVPR*

abstract: Adversarial robustness has attracted extensive studies recently by revealing the vulnerability and intrinsic characteristics of deep networks. However, existing works on adversarial robustness mainly focus on balanced datasets, while real-world data usually exhibits a long-tailed distribution. To push adversarial robustness towards more realistic scenarios, in this work we investigate the adversarial vulnerability as well as defense under long-tailed distributions. In particular, we first reveal the negative impacts induced by imbalanced data on both recognition performance and adversarial robustness, uncovering the intrinsic challenges of this problem. We then perform a systematic study on existing long-tailed recognition methods in conjunction with the adversarial training framework.  Several valuable observations are obtained, 1) natural accuracy is relatively easy to improve, 2) fake gain of robust accuracy exists under unreliable evaluation, and 3) boundary error limits the promotion of robustness. Inspired by these observations, we propose a clean yet effective framework, RoBal, which consists of two dedicated modules, a scale-invariant classifier and data re-balancing via both margin engineering at training stage and boundary adjustment during inference. Extensive experiments demonstrate the superiority of our approach over other state-of-the-art defense methods.To our best knowledge, we are the first to tackle adversarial robustness under long-tailed distributions, which we believe would be a significant step towards real-world robustness.

# Summary. An optional shortened abstract.
summary: Accepted by IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021, as **<font color='#FF5722'>Oral</font>** <br> ***Tong Wu**, [Ziwei Liu](https://liuziwei7.github.io/), [Qingqiu Huang](http://qqhuang.cn/), [Yu Wang](http://nicsefc.ee.tsinghua.edu.cn/people/yu-wang/), [Dahua Lin](http://dahua.me/)*

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

