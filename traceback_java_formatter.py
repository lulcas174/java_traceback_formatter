import re
from typing import List, Optional


def format_java_traceback(raw_traceback: str, max_stack_lines: int = 10) -> str:
    lines = raw_traceback.strip().splitlines()
    traceback_blocks = []
    current_block = []

    for line in lines:
        if line.strip().startswith('Caused by:'):
            if current_block:
                traceback_blocks.append(current_block)
            current_block = [line]
        elif line.strip():
            current_block.append(line)
    
    if current_block:
        traceback_blocks.append(current_block)

    if not traceback_blocks:
        return ""

    if len(traceback_blocks) > 1:
        relevant_blocks = [traceback_blocks[0], traceback_blocks[-1]]
    else:
        relevant_blocks = traceback_blocks

    formatted_lines = []
    for i, block in enumerate(relevant_blocks):
        if i > 0:
            formatted_lines.append("\n[Root Cause]")
        
        exception_header = block[0].strip()
        formatted_lines.append(exception_header)

        stack_trace_line_count = 0
        for line in block[1:]:
            stripped_line = line.strip()
            if stripped_line.startswith('at '):
                if stack_trace_line_count < max_stack_lines:
                    formatted_lines.append(f"  {stripped_line}")
                    stack_trace_line_count += 1
            elif '... ' in stripped_line and ' more' in stripped_line:
                formatted_lines.append(f"  {stripped_line}")

    print("\n".join(formatted_lines))


