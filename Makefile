start:
	conda activate aia2

stop:
	conda deactivate

clean:
	@rm -f logs.txt
	@rm -fr __pycache__/
	@rm -fr players/__pycache__/

