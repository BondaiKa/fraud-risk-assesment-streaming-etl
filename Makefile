all: .development-environment

.development-environment:
	conda create --yes --copy --prefix .development-environment --channel defaults --override-channels python=3.10
	. $$(conda info --base)/etc/profile.d/conda.sh \
	&& conda activate ./.development-environment \
	&& pip install --force-reinstall --requirement requirements-dev.txt \
	&& conda deactivate


.PHONY: test
test:
	bash AZURE_APPCONFIG_CONNECTION_STRING="$AZURE_APPCONFIG_CONNECTION_STRING" AZURE_APPCONFIG_EVENT_HUB_NAME=kafka-transaction python3 ./kafka/dummy-producer.py  ./dummy-run.sh

.PHONY: clean
clean:
	rm -rf ./.development-environment