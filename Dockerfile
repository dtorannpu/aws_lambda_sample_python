FROM public.ecr.aws/lambda/python:3.12 AS builder

WORKDIR /work/src
RUN pip install --upgrade pip && pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt --without-hashes



FROM public.ecr.aws/lambda/python:3.12

# Copy requirements.txt
COPY --from=builder /work/src/requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Copy function code
COPY src ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "aws_lambda_sample_python.lambda_function.handler" ]
