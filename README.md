# 计算力学反问题札记

有限的观测能在多大程度上确定一个结构？这组札记用两个可运行的算例回答这个问题。一个从梁端静态响应反推分段刚度，另一个从振动频率反推弹簧刚度分布。正文给出模型假设、解析推导、相关文献和数值复核。

| 札记 | 可复现的结果 | 代码 |
| --- | --- | --- |
| [总刚度和固有频率都相同，弹簧分布还能不同吗？](spring_chain.md) | 在两端固定、三个单位质量和四根正刚度弹簧的模型中，构造总刚度相同、彼此非镜像且具有相同频谱的配置。 | [`spring_chain.py`](spring_chain.py) |
| [只测梁端，能反推出多少段刚度？](beam_tip.md) | 在已知段界与完整静态端部柔度的条件下，三段可唯一识别。四段正刚度反例具有相同的端部柔度矩阵。 | [`beam_tip.py`](beam_tip.py) |

## 运行复现脚本

已在 Python 3.12.14、NumPy 2.3.5 环境运行。算例参数均已写在脚本中，无需下载实验数据。

```sh
python -m pip install -r requirements.txt
python beam_tip.py
python spring_chain.py
```

梁算例输出三段观测矩阵行列式 `2/729`、反解刚度、误差扰动结果，以及四段反例的相同观测。弹簧链算例输出共同特征多项式的系数，并分别计算两组刚度的特征值 `0.5, 2, 3.5`。

文中的结论适用于各自给定的模型和观测条件。与相关文献的具体重合范围及贡献说明见各篇正文。

## 仓库内容

| 文件 | 内容 |
|---|---|
| `spring_chain.md` / `spring_chain.py` | 札记 B 正文与复现脚本 |
| `beam_tip.md` / `beam_tip.py` | 札记 C 正文与复现脚本 |
| `requirements.txt` | 复现所需的唯一依赖（NumPy） |

正文使用 LaTeX 数学式，在 GitHub 页面直接渲染。脚本只依赖 NumPy，结论以断言形式写在脚本里，任一结论不成立会直接抛 `AssertionError`。

## 作者

**林卫叙**

两篇札记由作者在 AI 工具辅助下完成，全部技术结论经作者核验。具体分工见各篇末尾的「复现与贡献说明」。

## 相关工作

同一位作者关于鱼竿变形曲线识别的开源工具：[rod-curve-vision](https://github.com/99999vvain/rod-curve-vision)。

## 引用

```bibtex
@misc{cm_notes_2026,
  title  = {计算力学反问题札记},
  author = {林卫叙},
  year   = {2026},
  note   = {两篇可复现的计算力学反问题札记},
  url    = {https://github.com/99999vvain/computational-mechanics-notes}
}
```

## 许可证

MIT，见 [LICENSE](LICENSE)。
