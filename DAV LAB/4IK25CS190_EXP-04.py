{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RkiYZPVyZkIW"
      },
      "outputs": [],
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "import pandas as pd\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"/content/student_performance_dataset.csv\")\n",
        "\n",
        "print(\"First 5 rows of dataset:\")\n",
        "\n",
        "print(df.head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z7xg62NKZ9Hd",
        "outputId": "54f7846d-cdb2-4b9c-c6fe-ffa2a69ae605"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First 5 rows of dataset:\n",
            "  Student_ID  Gender  Study_Hours_per_Week  Attendance_Rate  Past_Exam_Scores  \\\n",
            "0       S147    Male                    31        68.267841                86   \n",
            "1       S136    Male                    16        78.222927                73   \n",
            "2       S209  Female                    21        87.525096                74   \n",
            "3       S458  Female                    27        92.076483                99   \n",
            "4       S078  Female                    37        98.655517                63   \n",
            "\n",
            "  Parental_Education_Level Internet_Access_at_Home Extracurricular_Activities  \\\n",
            "0              High School                     Yes                        Yes   \n",
            "1                      PhD                      No                         No   \n",
            "2                      PhD                     Yes                         No   \n",
            "3                Bachelors                      No                         No   \n",
            "4                  Masters                      No                        Yes   \n",
            "\n",
            "   Final_Exam_Score Pass_Fail  \n",
            "0                63      Pass  \n",
            "1                50      Fail  \n",
            "2                55      Fail  \n",
            "3                65      Pass  \n",
            "4                70      Pass  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nDataset Info:\")\n",
        "\n",
        "print(df.info())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xvi7IMbCasHA",
        "outputId": "ceef9aa6-c2d6-4151-b9ca-70611b81b17e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Dataset Info:\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 708 entries, 0 to 707\n",
            "Data columns (total 10 columns):\n",
            " #   Column                      Non-Null Count  Dtype  \n",
            "---  ------                      --------------  -----  \n",
            " 0   Student_ID                  708 non-null    object \n",
            " 1   Gender                      708 non-null    object \n",
            " 2   Study_Hours_per_Week        708 non-null    int64  \n",
            " 3   Attendance_Rate             708 non-null    float64\n",
            " 4   Past_Exam_Scores            708 non-null    int64  \n",
            " 5   Parental_Education_Level    708 non-null    object \n",
            " 6   Internet_Access_at_Home     708 non-null    object \n",
            " 7   Extracurricular_Activities  708 non-null    object \n",
            " 8   Final_Exam_Score            708 non-null    int64  \n",
            " 9   Pass_Fail                   708 non-null    object \n",
            "dtypes: float64(1), int64(3), object(6)\n",
            "memory usage: 55.4+ KB\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nMissing values before handling:\")\n",
        "\n",
        "print(df.isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tNqcCwyQbEiy",
        "outputId": "29d1e8c7-a040-47cf-ecbc-27f021e4e5f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Missing values before handling:\n",
            "Student_ID                    0\n",
            "Gender                        0\n",
            "Study_Hours_per_Week          0\n",
            "Attendance_Rate               0\n",
            "Past_Exam_Scores              0\n",
            "Parental_Education_Level      0\n",
            "Internet_Access_at_Home       0\n",
            "Extracurricular_Activities    0\n",
            "Final_Exam_Score              0\n",
            "Pass_Fail                     0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.loc[0:5, 'Study_Hours_per_Week'] = None\n",
        "\n",
        "df.loc[10:15, 'Attendance_Rate'] = None\n",
        "\n",
        "df.loc [20:25, 'Past_Exam_Scores'] = None\n",
        "\n",
        "df.loc[30:35, 'Final_Exam_Score'] = None\n",
        "\n",
        "print(\"\\nMissing values after inserting sample NaNs:\")\n",
        "\n",
        "print(df.isnull().sum() [df.isnull().sum() > 0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5d2sp4EfbHr6",
        "outputId": "9023a16e-916e-4b51-cd77-b056fbbe8a9a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Missing values after inserting sample NaNs:\n",
            "Study_Hours_per_Week    6\n",
            "Attendance_Rate         6\n",
            "Past_Exam_Scores        6\n",
            "Final_Exam_Score        6\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Study_Hours_per_Week']=df['Study_Hours_per_Week'].fillna(df['Study_Hours_per_Week'].mean())"
      ],
      "metadata": {
        "id": "iOaBuCThcM3W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Attendance_Rate']= df['Attendance_Rate'].fillna(df['Attendance_Rate'].median())"
      ],
      "metadata": {
        "id": "KD5_VYXrdDRB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Past_Exam_Scores']=df['Past_Exam_Scores'].fillna(df['Past_Exam_Scores'].mean())\n",
        "print(\"\\nMissing values after imputation\")\n",
        "print(df.isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hMneanfYdmlf",
        "outputId": "a3a2d2a1-c049-4877-eda5-7092dcc398b0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Missing values after imputation\n",
            "Student_ID                    0\n",
            "Gender                        0\n",
            "Study_Hours_per_Week          0\n",
            "Attendance_Rate               0\n",
            "Past_Exam_Scores              0\n",
            "Parental_Education_Level      0\n",
            "Internet_Access_at_Home       0\n",
            "Extracurricular_Activities    0\n",
            "Final_Exam_Score              6\n",
            "Pass_Fail                     0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\none-Hot Encoded columns\")\n",
        "print(df.columns.tolist())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5Dxv6f5IeHFG",
        "outputId": "b0c55e77-4b0f-4a9c-b146-22cec299e826"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "one-Hot Encoded columns\n",
            "['Student_ID', 'Gender', 'Study_Hours_per_Week', 'Attendance_Rate', 'Past_Exam_Scores', 'Parental_Education_Level', 'Internet_Access_at_Home', 'Extracurricular_Activities', 'Final_Exam_Score', 'Pass_Fail']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "le=LabelEncoder()\n",
        "df['Pass_Fail_Encoded']=le.fit_transform(df['Pass_Fail'])\n",
        "print(\"\\nLabel Encoded Result\")\n",
        "print(df[['Pass_Fail','Pass_Fail_Encoded']].head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "I2zCxiJwedBz",
        "outputId": "343b233d-c36c-4267-a1f7-8b11e46f4176"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Label Encoded Result\n",
            "  Pass_Fail  Pass_Fail_Encoded\n",
            "0      Pass                  1\n",
            "1      Fail                  0\n",
            "2      Fail                  0\n",
            "3      Pass                  1\n",
            "4      Pass                  1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Gender_Encoded']= le.fit_transform(df['Gender'])\n",
        "df['Internet_Access_Encoded']= le.fit_transform(df['Internet_Access_at_Home'])\n",
        "df['Extracurricular_Activities_Encoded']=le.fit_transform(df['Extracurricular_Activities'])\n"
      ],
      "metadata": {
        "id": "6mgG3piefARG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.to_csv(\"student_performance_cleaned.csv\",index=False)\n",
        "print(\"\\nCleaned dataset saved as 'student_performance_cleaned.csv'\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_US0wixefgT-",
        "outputId": "2316e45b-2212-4452-eba3-d411372a39fd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Cleaned dataset saved as 'student_performance_cleaned.csv'\n"
          ]
        }
      ]
    }
  ]
}