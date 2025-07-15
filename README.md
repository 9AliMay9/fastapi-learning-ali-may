# FastAPI Learning - Ali May

> 🚀 This repository records my FastAPI learning journey and practice code.

---

## 项目简介 / Project Description

这是 Ali May 的 FastAPI 学习笔记与示例代码集合，旨在通过实战掌握 FastAPI 核心机制、依赖注入、中间件、响应模型等知识点。

This repository contains FastAPI learning notes and example codes by Ali May, aiming to master FastAPI core features, dependency injection, middleware, response models, and more through hands-on practice.

---

## 环境准备 / Environment Setup

* Python 3.11+
* [PDM](https://pdm.fming.dev/) for dependency management
* VSCode or any preferred IDE
* WSL2 (optional, for Windows users)

---

## 快速开始 / Quick Start

```bash
git clone https://github.com/9AliMay9/fastapi-learning-ali-may.git
cd fastapi-learning-ali-may
pdm install
pdm run uvicorn main:app --reload
```

访问 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 查看自动生成的 Swagger UI。

---

## 目录结构 / Project Structure

```
fastapi-learning-ali-may/
├── main.py               # FastAPI 主程序
├── README.md             # 本说明文件
├── pyproject.toml        # PDM 配置文件
└── .venv/                # 虚拟环境文件夹（忽略上传）
```

---

## 已学内容 / Completed Topics

* FastAPI 基础路由与请求处理
* Pydantic 模型与数据验证
* 依赖注入（Depends）机制
* 中间件基础示例
* 响应模型与字段控制（include / exclude）
* 错误处理与 HTTPException
* POST/GET 请求示例

---

## 后续计划 / Next Steps

* 学习 SQLModel/SQLAlchemy 与数据库操作
* 掌握 OAuth2 + JWT 认证机制
* 探索 Docker 容器化与部署
* 构建完整任务管理 API 项目

---

## 联系 / Contact

欢迎提出建议和交流！

GitHub: [https://github.com/9AliMay9](https://github.com/9AliMay9)
Email: 2628839532@qq.com

---

## 版权声明 / License

本项目采用 MIT 许可证，详见 LICENSE 文件。

---

### 备注

* 以上命令中的 `pdm` 是项目依赖管理工具，确保你已安装并配置好。
* WSL2 是 Windows 用户推荐的 Linux 子系统环境，非必需。
