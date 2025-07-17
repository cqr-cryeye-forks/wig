def transform_json(data: list) -> list:
    result = []

    for entry in data:
        site_info = entry.get("site_info", {})
        statistics = entry.get("statistics")
        parsed_entry = {}

        if (
            "error" in site_info
            and set(site_info.keys()) <= {"url", "error"}
        ):
            result.append(site_info)
            continue

        # Пропускаем, если нет statistics или url
        if not statistics or "url" not in site_info:
            continue

        parsed_entry["url"] = site_info["url"]

        if title := site_info.get("title"):
            parsed_entry["title"] = title

        if cookies := site_info.get("cookies"):
            if isinstance(cookies, list) and cookies:
                parsed_entry["cookies"] = cookies

        if ips := site_info.get("ip"):
            if isinstance(ips, list) and ips:
                parsed_entry["ip"] = ips

        if data_list := entry.get("data"):
            if isinstance(data_list, list):
                transformed_data = []
                for d in data_list:
                    cat = d.get("category")
                    if cat == "Interesting":
                        url = d.get("url", "")
                        note = d.get("note", "")
                        if url or note:
                            transformed_data.append(f"[Interesting] {url} — {note}".strip())
                    elif cat:
                        name = d.get("name", "")
                        version = d.get("version", "")
                        if version:
                            transformed_data.append(f"[{cat}] {name} v{version}".strip())
                        elif name:
                            transformed_data.append(f"[{cat}] {name}".strip())
                if transformed_data:
                    parsed_entry["data"] = transformed_data

        parsed_entry["urls"] = statistics.get("urls")
        parsed_entry["fingerprints"] = statistics.get("fingerprints")

        result.append(parsed_entry)

    return result
