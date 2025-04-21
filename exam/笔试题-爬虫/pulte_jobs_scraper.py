import requests
import csv
import json
import time

def scrape_jobs():
    base_url = "https://pultegroup.wd1.myworkdayjobs.com/wday/cxs/pultegroup/PGI/jobs"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # 初始化CSV文件，使用utf-8-sig编码来正确处理中文
    with open('pulte_jobs.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['职位名称', '工作地点', '职位类型', '发布日期']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        offset = 0
        limit = 20
        
        while True:
            print(f"正在获取第 {offset//limit + 1} 页数据...")
            
            # 构建请求数据
            data = {
                "appliedFacets": {},
                "limit": limit,
                "offset": offset,
                "searchText": ""
            }
            
            try:
                response = requests.post(base_url, headers=headers, json=data)
                response.raise_for_status()
                
                jobs_data = response.json()
                total = jobs_data.get('total', 0)
                jobs = jobs_data.get('jobPostings', [])
                
                if not jobs:
                    print("没有更多职位信息")
                    break
                
                print(f"找到 {len(jobs)} 个职位")
                
                for job in jobs:
                    try:
                        title = job.get('title', '未知职位')
                        location = job.get('locationsText', '未知地点')
                        job_type = job.get('timeType', '未指定')
                        posted_date = job.get('postedOn', '未指定')
                        
                        # 处理发布日期格式
                        if posted_date.startswith('Posted'):
                            posted_date = posted_date.strip()
                        
                        job_info = {
                            '职位名称': title,
                            '工作地点': location,
                            '职位类型': job_type,
                            '发布日期': posted_date
                        }
                        writer.writerow(job_info)
                        print(f"已保存职位: {title} - {location}")
                    except Exception as e:
                        print(f"处理职位信息时出错: {e}")
                        continue
                
                if offset + limit >= total:
                    print("已到达最后一页")
                    break
                
                offset += limit
                time.sleep(2)  # 添加延迟以避免请求过于频繁
                
            except requests.exceptions.RequestException as e:
                print(f"请求出错: {e}")
                break
            except json.JSONDecodeError as e:
                print(f"解析JSON响应时出错: {e}")
                break
            except Exception as e:
                print(f"发生错误: {e}")
                break

if __name__ == "__main__":
    print("开始抓取Pulte Group职位信息...")
    scrape_jobs()
    print("职位信息已保存到 pulte_jobs.csv") 