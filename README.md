# Data Engineering Golden Template

This repository is a **personal reusable template** for data engineering projects, covering:

- Batch processing (Spark)
- Streaming (Kafka + Spark)
- Orchestration (Airflow)
- Version-locked dependencies for stable environments

---

## 1️⃣ Prerequisites

Make sure your machine has:

- **Docker Desktop** (with WSL2 backend for Windows)
- **Git** (for cloning and version control)
- Optional: Python 3.9 for local scripts
- Minimum 8GB RAM recommended

---

## 2️⃣ Clone the Repo

```bash
git clone https://github.com/Ailurophile47/data-engineering-template.git
cd data-engineering-template
```

---

## 3️⃣ Versions Locked

See `versions.md` for all pinned versions.
This ensures **repeatable and stable setups**.

**Key versions**:

| Component | Version |
| --------- | ------- |
| Python    | 3.9     |
| Spark     | 3.4.1   |
| PySpark   | 3.4.1   |
| Pandas    | 1.5.3   |
| Airflow   | 2.7.3   |
| Postgres  | 13      |
| Kafka     | 3.4.x   |
| Zookeeper | 3.8.x   |

---

## 4️⃣ Airflow Setup

### 4.1 Start Airflow

We use **Docker Compose** for Airflow + Postgres:

```bash
docker compose up -d
```

This will start:

- Postgres metadata DB
- Airflow Webserver (port 8080)
- Airflow Scheduler

---

### 4.2 Airflow CLI

Access the Airflow container:

```bash
docker exec -it airflow_webserver /bin/bash
```

Common commands:

- Initialize DB (first-time only):

```bash
airflow db init
```

- List DAGs:

```bash
airflow dags list
```

- Trigger a DAG:

```bash
airflow dags trigger <dag_id>
```

- Monitor DAG runs:

```bash
airflow dags list-runs -d <dag_id>
```

- Start scheduler manually (if needed):

```bash
airflow scheduler
```

---

### 4.3 Web UI

Open browser:

```
http://localhost:8080
```

Default credentials:

- Username: `airflow`
- Password: `airflow`

---

## 5️⃣ Kafka + Spark Streaming

### 5.1 Start Kafka

```bash
docker compose -f kafka/docker-compose.kafka.yml up -d
```

- Zookeeper → 2181
- Kafka broker → 9092
- Kafka advertised listener → localhost:9092

Check logs:

```bash
docker compose -f kafka/docker-compose.kafka.yml logs -f kafka
```

---

### 5.2 Spark Streaming Job

Run Spark job inside Docker or your local Spark setup:

```bash
python spark/streaming/kafka_stream.py
```

- Reads from Kafka topic `test-topic.`
- Prints streaming data to console

---

### 5.3 Kafka CLI (optional)

- List topics:

```bash
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
```

- Create topic:

```bash
docker exec -it kafka kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

- Produce messages:

```bash
docker exec -it kafka kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
```

- Consume messages:

```bash
docker exec -it kafka kafka-console-consumer --topic test-topic --bootstrap-server localhost:9092 --from-beginning
```

---

## 6️⃣ Spark Batch Jobs

- Place your ETL scripts in `spark/batch/.`
- Example:

```bash
python spark/batch/etl_job.py
```

- Use **PySpark** API consistent with pinned Spark version 3.4.1
- Version compatibility guaranteed via Docker / PySpark pins

---

## 7️⃣ Notes & Best Practices

- **Do not upgrade versions casually** — update `versions.md` first
- Docker is the **source of truth**
- Commit one logical change per Git commit
- Use the `airflow/dags` folder to place all DAGs
- Keep streaming code in `spark/streaming/` and batch code in `spark/batch/.`
- Use `.gitignore` to prevent logs, `.pyc` files, and local environment leaks

---

## 8️⃣ Useful CLI Commands Summary

```bash
# Git
git clone <repo_url>
git status
git add.
git commit -m "message."
git push -u origin main

# Airflow
docker compose up -d
docker exec -it airflow_webserver /bin/bash
airflow db init
airflow dags list
airflow dags trigger <dag_id>

# Kafka
docker compose -f kafka/docker-compose.kafka.yml up -d
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

# Spark
python spark/batch/etl_job.py
python spark/streaming/kafka_stream.py
```

---
---

> ⚠️ Always refer to `versions.md` before adding new libraries or upgrading any component.
