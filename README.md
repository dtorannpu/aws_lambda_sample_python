# AWS Lambda Python サンプル

## コンテナビルド

```bash
docker build --platform linux/amd64 -t docker-image:test .
```


## ローカル実行

```bash
docker run --platform linux/amd64 -p 9000:8080 docker-image:test
```


## ローカル呼び出し

```bash
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```


