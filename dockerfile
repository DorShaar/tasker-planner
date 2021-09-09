FROM python:3.8 AS builder

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt

# Tests.
RUN python -m unittest tests/domain/testStringReplacer.py
RUN python -m unittest tests/infra/testUserQuestioner.py

# second unnamed stage
FROM python:3.8-slim
WORKDIR /app

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /app/package/ /app/package/
COPY --from=builder /app/plan.json /app/plan.json

CMD [ "python", "./package/taskerPlanner.py" ]
