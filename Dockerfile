FROM python:3.10-alpine AS builder

WORKDIR /invoke-workflow

COPY ./requirements.txt .

RUN pip3 install -r ./requirements.txt -t .

FROM gcr.io/distroless/python3 as invoke-workflow

COPY --from=builder /invoke-workflow /invoke-workflow

WORKDIR /invoke-workflow

COPY . .

ENTRYPOINT ["python3"]
CMD ["/invoke-workflow/main.py"]